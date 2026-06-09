import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration for full edge-to-edge screen usage
st.set_page_config(page_title="Ireland Work Permits Dashboard", layout="wide")

st.title("🇮🇪 Ireland Employment Permits Analytics Dashboard")
# Updated Subtitle displaying the maximum data timeframe dynamically
st.markdown("##### 📅 *Data current as of: May 2026*")
st.markdown("Fuzzy search corporate entities or isolate records dynamically using column-level constraints below.")

# 2. Dynamic Parsing Pipeline
@st.cache_data
def load_and_clean_data():
    # Absolute raw string path to avoid slash execution or spacing bugs on Windows
    df = pd.read_excel(r"C:\Users\Ting's\Desktop\JobHunting\Stats (2021-2026)\Stats 2021-2026 onwards.xlsx")
    
    years = [2021, 2022, 2023, 2024, 2025, 2026]
    cleaned_data = []

    for year in years:
        target_emp_col = None
        target_perm_col = None
        
        for col_idx in range(df.shape[1]):
            col_content = df.iloc[:, col_idx].astype(str)
            col_name = str(df.columns[col_idx])
            
            if (str(year) in col_name or col_content.str.contains(str(year), na=False).any()) and \
               (col_name.lower().find("employer") != -1 or col_content.str.contains("Employer", case=False, na=False).any()):
                if target_emp_col is None:
                    target_emp_col = col_idx
                    target_perm_col = col_idx + 1 
                    break
        
        if target_emp_col is None:
            idx = years.index(year)
            target_emp_col = idx * 2
            target_perm_col = (idx * 2) + 1

        if target_emp_col < df.shape[1] and target_perm_col < df.shape[1]:
            year_df = df.iloc[:, [target_emp_col, target_perm_col]].dropna()
            year_df.columns = ['Employer', 'Permits']
            year_df = year_df[~year_df['Employer'].astype(str).str.contains('Total|Grand|Employer|Permits', case=False, na=False)]
            year_df['Year'] = year
            cleaned_data.append(year_df)

    final_df = pd.concat(cleaned_data, ignore_index=True)
    
    final_df['Permits'] = final_df['Permits'].astype(str).str.replace(',', '').str.strip()
    final_df['Permits'] = pd.to_numeric(final_df['Permits'], errors='coerce')
    final_df = final_df.dropna(subset=['Permits'])
    final_df['Permits'] = final_df['Permits'].astype(int)
    final_df['Employer'] = final_df['Employer'].astype(str).str.strip()
    
    return final_df

try:
    df = load_and_clean_data()
except Exception as e:
    st.error(f"Data mapping execution failed. Verify file alignment. Details: {e}")
    st.stop()


# ==========================================
# 1. TIMEFRAME FILTERING OPTIONS
# ==========================================
with st.expander("📅 Timeframe Filtering Options", expanded=True):
    all_years = sorted(df['Year'].unique())
    selected_years = st.multiselect(
        "Isolate Dashboard Data Timeline Ranges:", 
        options=all_years, 
        default=all_years
    )

if selected_years:
    global_filtered_df = df[df['Year'].isin(selected_years)]
else:
    global_filtered_df = df.copy()


# ==========================================
# 2. OPTIMIZED EMPLOYER GROUP SEARCH
# ==========================================
st.markdown("## 🔍 Employer Group Search")
search_query = st.text_input(
    "Type keyword to find all associated subsidiary entities (e.g., Google, Care, NHS, Bank):", 
    value="", 
    placeholder="Type here to filter..."
).strip()

if search_query:
    search_filtered_df = global_filtered_df[global_filtered_df['Employer'].str.contains(search_query, case=False, na=False)]
    
    if not search_filtered_df.empty:
        st.success(f"Found {search_filtered_df['Employer'].nunique()} distinct entities matching '{search_query}'")
        
        spot1, spot2 = st.columns([2, 3])
        
        with spot1:
            st.markdown("### 📈 Aggregated Trend Line")
            trend_group = search_filtered_df.groupby('Year')['Permits'].sum().reset_index()
            trend_group['Year'] = trend_group['Year'].astype(str)
            
            fig_search = px.line(
                trend_group, x='Year', y='Permits', text='Permits', markers=True,
                title=f"Total Permits Trend combined for '{search_query}'", template='plotly_white'
            )
            fig_search.update_traces(textposition="top center")
            st.plotly_chart(fig_search, use_container_width=True)
            
        with spot2:
            st.markdown(f"### 📋 Annual Volume Matrix for '{search_query}'")
            matrix_pivot = search_filtered_df.pivot_table(
                index='Employer', 
                columns='Year', 
                values='Permits', 
                aggfunc='sum', 
                fill_value=0
            ).reset_index()
            
            matrix_pivot['Total'] = matrix_pivot.iloc[:, 1:].sum(axis=1)
            sorted_matrix = matrix_pivot.sort_values(by='Total', ascending=False)
            
            # Convert all data table headers to text strings first to avoid NumPy JSON encoder bugs
            sorted_matrix.columns = [str(col) for col in sorted_matrix.columns]
            
            # Explicit pixel allocation parameters to crush layout overflow and scrollbars completely
            column_configs = {
                "Employer": st.column_config.TextColumn("Employer Name", width=260),
                "Total": st.column_config.NumberColumn("Total", width=65)
            }
            
            # Force target year strings to lock into a tight 60px viewport grid
            for yr in all_years:
                column_configs[str(yr)] = st.column_config.NumberColumn(str(yr), width=60)
                
            st.dataframe(
                sorted_matrix, 
                hide_index=True, 
                use_container_width=True,
                column_config=column_configs
            )
    else:
        st.warning(f"No company entries found matching '{search_query}' under the current year parameters.")

st.markdown("---")


# ==========================================
# 3. MACRO SYSTEM OVERVIEW (MAXIMIZED VISUALS)
# ==========================================
st.markdown("## 📊 Macro Market Overview")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Permits within Parameters", value=f"{global_filtered_df['Permits'].sum():,}")
with col2:
    st.metric(label="Total Sponsoring Corporate Entities", value=f"{global_filtered_df['Employer'].nunique():,}")

st.subheader("🏭 Top 10 Volume Employers")
if not global_filtered_df.empty:
    top_macro = global_filtered_df.groupby('Employer')['Permits'].sum().reset_index().sort_values(by='Permits', ascending=False).head(10)
    fig_macro_bar = px.bar(
        top_macro, 
        x='Permits', 
        y='Employer', 
        orientation='h', 
        text_auto=',',
        template='plotly_white', 
        color_discrete_sequence=['#2ca02c'],
        height=450 
    )
    fig_macro_bar.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_macro_bar, use_container_width=True)
else:
    st.info("No global data records match selection criteria.")

st.markdown("---")

chart_bottom, grid_bottom = st.columns([1, 1])
with chart_bottom:
    st.subheader("Overall Market Trend Line")
    macro_trend = global_filtered_df.groupby('Year')['Permits'].sum().reset_index()
    macro_trend['Year'] = macro_trend['Year'].astype(str)
    st.plotly_chart(px.bar(macro_trend, x='Year', y='Permits', text_auto=',', template='plotly_white'), use_container_width=True)

with grid_bottom:
    st.subheader("📋 Raw Data Records Grid")
    
    # Isolated control row positioned neatly over the grid element
    grid_ctrl1, grid_ctrl2 = st.columns([1, 2])
    with grid_ctrl1:
        year_search = st.selectbox("Isolate Grid Year:", ["All Years"] + [str(y) for y in all_years])
    with grid_ctrl2:
        emp_search = st.text_input("Isolate Grid Employer Name:", placeholder="Type to filter rows below...")

    # Filtering rows down based on the inputs above
    grid_df = global_filtered_df.copy()
    if year_search != "All Years":
        grid_df = grid_df[grid_df['Year'].astype(str) == year_search]
    if emp_search:
        grid_df = grid_df[grid_df['Employer'].str.contains(emp_search, case=False, na=False)]

    display_grid_df = grid_df[['Year', 'Employer', 'Permits']].copy()
    display_grid_df.columns = ['Year', 'Employer Name', 'Permits Issued']
    display_grid_df['Year'] = display_grid_df['Year'].astype(str)
    
    st.dataframe(
        display_grid_df.sort_values(by=['Year', 'Permits Issued'], ascending=[False, False]), 
        use_container_width=True, 
        hide_index=True, 
        height=300,
        column_config={
            "Year": st.column_config.TextColumn("Year", width="small"),
            "Employer Name": st.column_config.TextColumn("Employer Name", width="large"),
            "Permits Issued": st.column_config.NumberColumn("Permits Issued", width="small")
        }
    )
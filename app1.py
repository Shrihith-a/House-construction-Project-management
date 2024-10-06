import streamlit as st
import pandas as pd
import plotly.express as px

# Sample Data for Gantt Chart
tasks = {
    'Task': ['Clear Site', 'Set Up Temporary Facilities', 'Survey and Mark Boundaries', 'Excavate Foundation', 
             'Pour Concrete Footings', 'Install Foundation Walls', 'Erect Structural Framework', 
             'Install Roof Trusses', 'Install Exterior Walls', 'Structural Inspection', 'Install Plumbing', 
             'Install Electrical Wiring', 'Drywall Installation', 'Painting and Finishing', 'Install Fixtures', 
             'Interior Inspection', 'Prepare Soil and Plant Grass', 'Install Irrigation System', 'Final Inspection', 
             'Handover to Client'],
    'Start': ['2024-10-01', '2024-10-06', '2024-10-11', '2024-11-01', '2024-11-11', '2024-11-21', '2024-12-01', 
              '2024-12-21', '2025-01-01', '2025-01-16', '2025-02-01', '2025-03-01', '2025-04-01', '2025-04-16', 
              '2025-05-01', '2025-05-16', '2025-06-01', '2025-06-16', '2025-07-01', '2025-07-16'],
    'Finish': ['2024-10-04', '2024-10-10', '2024-10-16', '2024-11-08', '2024-11-15', '2024-11-26', '2024-12-11', 
               '2024-12-27', '2025-01-06', '2025-01-19', '2025-02-10', '2025-03-03', '2025-04-09', '2025-04-18', 
               '2025-05-04', '2025-05-23', '2025-06-03', '2025-06-23', '2025-07-05', '2025-07-26'],
    'Complete in %': [100, 100, 100, 25, 20, 10, 25, 15, 12, 50, 5, 10, 12, 13, 20, 16, 30, 20, 0, 0]
}
df_tasks = pd.DataFrame(tasks)

# Create Gantt Chart
fig_gantt = px.timeline(df_tasks, x_start='Start', x_end='Finish', y='Task', color='Complete in %', title='Task Overview')
fig_gantt.update_layout(title_font_size=20, font_size=12, title_font_family='Arial', yaxis={'autorange': 'reversed'})

# Sample Data for Bar Chart
data_bar = {'Task': tasks['Task'][:4], 'Complete in %': tasks['Complete in %'][:4]}
df_bar = pd.DataFrame(data_bar)
fig_bar = px.bar(df_bar, x='Task', y='Complete in %', title='Task Completion Status')

# Sample Data for Line Chart
data_line = {'Date': ['2024-10-01', '2024-10-06', '2024-10-11', '2024-11-01'], 'Completion': [10, 20, 30, 40]}
df_line = pd.DataFrame(data_line)
fig_line = px.line(df_line, x='Date', y='Completion', title='Project Progress Over Time')

# Sample Data for Pie Chart
fig_pie = px.pie(df_bar, names='Task', values='Complete in %', title='Task Completion Distribution')

# Sample Data for Scatter Plot
fig_scatter = px.scatter(df_tasks, x='Start', y='Finish', text='Task', title='Task Start and Finish Dates')

# Streamlit App
st.set_page_config(page_title="House Construction Project Dashboard", layout="wide")

st.title("🏠 House Construction Project Management Dashboard")
st.markdown("### A comprehensive view of the project's progress and status")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gantt Chart")
    st.plotly_chart(fig_gantt, use_container_width=True)

    st.subheader("Line Chart")
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("Bar Chart")
    st.plotly_chart(fig_bar, use_container_width=True)

    st.subheader("Pie Chart")
    st.plotly_chart(fig_pie, use_container_width=True)

st.subheader("Scatter Plot")
st.plotly_chart(fig_scatter, use_container_width=True)

# Add some styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .css-18e3th9 {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .css-1d391kg {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)


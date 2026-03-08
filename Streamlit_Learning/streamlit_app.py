# streamlit run streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# st.write("hello world")
# st.header("button test")
# if st.button("Click me"):
#     st.write("you little jerk")
# else:
#     st.write("why you didn't click me?")
# add_sidebar=st.sidebar.selectbox("Add sidebar",["A","B","C"])
#
# if add_sidebar=="A":
#     st.write("what can i help you?")
# if add_sidebar=="B":
#     st.write("what can i help you?you little sweety?")
# if add_sidebar=="C":
#     st.write("what can i help you?you little dumbass?")
#
#
# col1, col2, col3 = st.columns(3)
#
# with col1:
#     st.metric(label="股票价格", value="120.50 USD", delta="1.20 USD")
#
# with col2:
#     st.metric(label="活跃用户", value="5.2 K", delta="-5%", delta_color="inverse")
#
# with col3:
#     st.metric(label="系统响应时间", value="25 ms", delta="0 ms")


st.header("Streamlit App")
st.write("hello! :sunglasses:")
st.write("666")
df=pd.DataFrame({"x":[1,2,3],"y":[4,5,6]})
st.write("dataframe:",df,"dataframe")

df2=pd.DataFrame(np.random.randn(200,3),columns=["a","b","c"])
c=alt.Chart(df2).mark_circle().encode(x='a',y='b',color='c',tooltip=['a','b','c'])
st.write(c)
'''
mark_circle()：指定使用圆形（气泡）来展示数据点。

encode(...)：将数据列映射到视觉属性上：

x='a', y='b'：确定点在横轴和纵轴的位置。

size='c'：根据 c 列的值决定圆圈的大小。

color='c'：根据 c 列的值决定颜色（通常会生成一个颜色渐变条）。

tooltip：交互关键。当你把鼠标悬停在某个点上时，会弹出一个小框显示该点具体的 a, b, c 数值。
'''




















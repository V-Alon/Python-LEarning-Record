import numpy as np
import plotly.graph_objects as go

# 生成参数网格（更密集的采样提升平滑度）
t = np.linspace(0, 2 * np.pi, 200)  # 方位角（绕z轴旋转）
s = np.linspace(0, np.pi, 200)      # 极角（与z轴的夹角）
t, s = np.meshgrid(t, s)

# 经典3D心形参数方程（数学验证过的正确形式）
x = 16 * np.sin(t)**3 * np.sin(s)
y = (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)) * np.sin(s)
z = 5 * (1 + np.cos(s))  # z范围：0（尖端）到10（顶部）

# 创建Plotly图形对象
fig = go.Figure(data=[
    go.Surface(
        x=x, y=y, z=z,
        colorscale='Reds',  # 红色渐变（可选'Viridis'/'Cividis'等）
        surfacecolor=z,     # 颜色随z轴高度变化
        cmin=0, cmax=10,    # 颜色映射范围（匹配z轴范围）
        showscale=False      # 隐藏颜色条
    )
])

# 配置布局（增强视觉效果）
fig.update_layout(
    title='Interactive 3D Heart',
    scene=dict(
        xaxis=dict(visible=False),  # 隐藏坐标轴
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectratio=dict(x=1, y=1, z=0.6),  # 调整长宽高比例（更接近真实心形）
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1)  # 初始视角（右前上方）
        )
    ),
    margin=dict(l=0, r=0, t=50, b=0)  # 减少边距
)

# 显示交互式图形（自动打开浏览器或Jupyter内渲染）
fig.show()
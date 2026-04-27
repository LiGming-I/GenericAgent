import streamlit as st
import yaml
from pathlib import Path

# 加载简历数据
resume_file = Path(__file__).parent / "resume.yaml"
with open(resume_file, encoding="utf-8") as f:
    data = yaml.safe_load(f)

# 页面设置
st.set_page_config(page_title=f"{data['name']} 的在线简历", layout="centered")

# 顶部个人信息
st.title(f"{data['name']} · {data['title']}")
cols = st.columns(3)
cols[0].markdown(f"📧 {data['email']}")
cols[1].markdown(f"📱 {data['phone']}")
cols[2].markdown(f"[💼 LinkedIn]({data['linkedin']})  |  [🐙 GitHub]({data['github']})")

# 个人简介
st.subheader("个人简介")
st.write(data["summary"])

# 技能关键词
st.subheader("技能")
st.write(" · ".join(data["skills"]))

# 工作经历
st.subheader("工作经历")
for exp in data["experiences"]:
    with st.expander(f"**{exp['role']}** @ {exp['company']}  ({exp['duration']})"):
        st.caption(f"📍 {exp['location']}")
        for item in exp["highlights"]:
            st.write(f"- {item}")

# 教育背景
st.subheader("教育背景")
for edu in data["education"]:
    st.write(f"**{edu['school']}** — {edu['degree']}  ({edu['duration']})")

# 侧边下载
with st.sidebar:
    st.download_button(
        label="📄 下载 PDF（示例）",
        data="PDF 生成需额外库，可先占位",
        file_name=f"{data['name']}_resume.pdf",
        mime="application/pdf",
    )
    st.info("改 `resume.yaml` → 保存 → 刷新页面即可实时更新简历")
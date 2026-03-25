---
name: 💡 Feature Request
description: Suggest a new feature or improvement
title: "[Feature]: "
labels: ["enhancement", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        感谢你提出功能建议！请详细描述你的想法。
  - type: textarea
    id: problem
    attributes:
      label: 相关需求
      description: 这个功能解决什么问题？
      placeholder: 清晰描述需求场景
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: 功能描述
      description: 你希望实现什么功能？
      placeholder: 详细描述期望的功能
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: 替代方案
      description: 你考虑过哪些替代方案？（可选）
  - type: textarea
    id: implementation
    attributes:
      label: 实现建议
      description: 你有实现思路吗？（可选）
      placeholder: 可能的技术方案或实现方式
  - type: textarea
    id: context
    attributes:
      label: 额外信息
      description: 其他补充说明、截图或参考链接
  - type: checkboxes
    id: will-contribute
    attributes:
      label: 贡献意愿
      options:
        - label: 我愿意参与这个功能的开发或测试

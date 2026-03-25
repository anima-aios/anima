---
name: 🐛 Bug Report
description: Report a bug or unexpected behavior
title: "[Bug]: "
labels: ["bug", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        感谢你报告问题！请尽量详细描述，帮助我们快速定位问题。
  - type: textarea
    id: description
    attributes:
      label: 问题描述
      description: 简要描述遇到的问题
      placeholder: 清晰简洁地描述问题是什么
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: 复现步骤
      description: 如何复现这个问题
      placeholder: |
        1. 安装 Anima...
        2. 运行命令...
        3. 看到错误...
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: 预期行为
      description: 你期望发生什么
      placeholder: 清晰描述预期结果
    validations:
      required: true
  - type: textarea
    id: actual
    attributes:
      label: 实际行为
      description: 实际发生了什么
      placeholder: 描述实际结果或错误信息
    validations:
      required: true
  - type: input
    id: os
    attributes:
      label: 操作系统
      placeholder: "e.g., macOS 14.0, Ubuntu 22.04, Windows 11"
    validations:
      required: true
  - type: input
    id: openclaw-version
    attributes:
      label: OpenClaw 版本
    validations:
      required: true
  - type: input
    id: anima-version
    attributes:
      label: Anima 版本
      placeholder: "e.g., v6.0.0"
    validations:
      required: true
  - type: input
    id: python-version
    attributes:
      label: Python 版本
      placeholder: "e.g., 3.9, 3.10, 3.11"
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: 日志/错误信息
      description: 如有错误日志或截图，请粘贴
      render: shell

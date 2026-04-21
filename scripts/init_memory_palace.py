#!/usr/bin/env python3
"""
h_k_mem 初始化脚本
分层记忆宫殿架构初始化工具
"""

import os
import sys
from pathlib import Path

def create_memory_palace(base_dir="."):
    """创建完整的记忆宫殿目录结构和模板文件"""
    
    # 创建记忆宫殿目录
    memory_palace_dir = Path(base_dir) / "记忆宫殿"
    memory_palace_dir.mkdir(exist_ok=True)
    
    print(f"📁 创建记忆宫殿目录: {memory_palace_dir}")
    
    # 各层模板内容
    templates = {
        "1F_项目任务区.md": """# 🏢 1F - 项目任务区 (入口大厅)
=======================
📍 位置：宫殿入口，中央喷泉
🔑 功能：存储当前项目任务信息

## 📋 当前任务
[在此添加当前项目任务]

## 📊 任务进度
- [ ] 任务1
- [ ] 任务2
- [ ] 任务3

## 🔗 相关文件
- [文件1]
- [文件2]
- [文件3]""",
        
        "2F_系统架构区.md": """# 🏢 2F - 系统架构区 (左翼)
=======================
📍 位置：宫殿左翼，橡木书架
🔑 功能：存储系统架构信息

## 📋 核心系统架构
[在此添加系统架构信息]

## 📁 文件结构
```
项目目录/
├── [目录1]
├── [目录2]
└── [目录3]
```""",
        
        "3F_数据分析区.md": """# 🏢 3F - 数据分析区 (右翼)
=======================
📍 位置：宫殿右翼，玻璃墙，数据大屏
🔑 功能：存储数据分析结果和发现

## 📊 数据分析结果
[在此添加数据分析结果]

## 🎯 关键发现
1. [发现1]
2. [发现2]
3. [发现3]""",
        
        "4F_用户要求区.md": """# 🏢 4F - 用户要求区 (二楼)
=======================
📍 位置：宫殿二楼，安静书房
🔑 功能：存储用户偏好和要求

## 📋 用户要求
[在此添加用户偏好和要求]

## ⚠️ 注意事项
- [注意事项1]
- [注意事项2]
- [注意事项3]""",
        
        "5F_文件管理区.md": """# 🏢 5F - 文件管理区 (三楼)
=======================
📍 位置：宫殿三楼，文件柜，归档系统
🔑 功能：存储文件路径和存储策略

## 📋 文件存储策略
[在此添加文件管理策略]

## 🔧 工具使用规范
1. [规范1]
2. [规范2]
3. [规范3]""",
        
        "B1_记忆管理区.md": """# 🏢 B1 - 记忆管理区 (地下室)
=======================
📍 位置：宫殿地下室，档案室，索引系统
🔑 功能：存储记忆管理方法和优化策略

## 📋 记忆管理原则
[在此添加记忆管理方法]

## 🔄 更新流程
1. [流程1]
2. [流程2]
3. [流程3]"""
    }
    
    # 创建各层文件
    created_files = []
    for filename, content in templates.items():
        file_path = memory_palace_dir / filename
        file_path.write_text(content, encoding='utf-8')
        created_files.append(filename)
        print(f"  📄 创建: {filename}")
    
    # 创建记忆索引内容
    memory_index = """🏛️ 记忆宫殿索引系统
===================
📍 架构：五层建筑+地下室（索引层）
🔑 访问：索引→文件→详细内容
📊 原则：索引化、分层化、文件化

📁 索引结构：
1F - 项目任务索引 → /记忆宫殿/1F_项目任务区.md
2F - 系统架构索引 → /记忆宫殿/2F_系统架构区.md  
3F - 数据分析索引 → /记忆宫殿/3F_数据分析区.md
4F - 用户要求索引 → /记忆宫殿/4F_用户要求区.md
5F - 文件管理索引 → /记忆宫殿/5F_文件管理区.md
B1 - 记忆管理索引 → /记忆宫殿/B1_记忆管理区.md

🔗 访问方式：
1. 查看索引 → 记忆宫殿索引
2. 查看详细 → 读取对应记忆文件
3. 更新内容 → 修改记忆文件
4. 同步索引 → 更新索引引用"""
    
    # 保存索引文件
    index_path = memory_palace_dir / "记忆宫殿索引.md"
    index_path.write_text(memory_index, encoding='utf-8')
    created_files.append("记忆宫殿索引.md")
    print(f"  📄 创建: 记忆宫殿索引.md")
    
    # 创建使用说明
    readme_content = """# 🏛️ 记忆宫殿使用指南

## 🎯 概述
记忆宫殿是一个分层记忆管理系统，突破Hermes Agent 2,200字符限制。

## 📁 目录结构
```
记忆宫殿/
├── 记忆宫殿索引.md      # 索引系统
├── 1F_项目任务区.md     # 项目任务信息
├── 2F_系统架构区.md     # 系统架构信息
├── 3F_数据分析区.md     # 数据分析结果
├── 4F_用户要求区.md     # 用户偏好要求
├── 5F_文件管理区.md     # 文件管理策略
└── B1_记忆管理区.md     # 记忆管理方法
```

## 🔧 使用方法
1. **查看索引**: 读取记忆宫殿索引.md
2. **访问内容**: 根据索引读取对应文件
3. **更新内容**: 修改对应记忆文件
4. **同步索引**: 必要时更新索引引用

## 📊 性能优势
- **容量扩展**: 35倍+存储能力
- **快速访问**: 索引化导航
- **易于维护**: 分层管理
- **可扩展性**: 随时添加新层

## 🔄 更新流程
1. 确定需要更新的内容类型
2. 找到对应的记忆文件
3. 修改文件内容
4. 检查索引是否需要更新

## 📞 支持
- GitHub: [项目地址]
- 作者: joez112
- 邮箱: 27816@qq.com"""
    
    readme_path = memory_palace_dir / "README.md"
    readme_path.write_text(readme_content, encoding='utf-8')
    created_files.append("README.md")
    print(f"  📄 创建: README.md")
    
    print(f"\n✅ 记忆宫殿初始化完成!")
    print(f"📁 总创建文件: {len(created_files)}个")
    print(f"📊 存储容量: 从2,200字符扩展到约10,000+字符")
    
    return {
        "directory": str(memory_palace_dir),
        "files": created_files,
        "memory_index": memory_index
    }

def check_memory_palace(base_dir="."):
    """检查记忆宫殿状态"""
    memory_palace_dir = Path(base_dir) / "记忆宫殿"
    
    if not memory_palace_dir.exists():
        print("❌ 记忆宫殿目录不存在")
        return False
    
    print(f"📁 记忆宫殿目录: {memory_palace_dir}")
    
    files = list(memory_palace_dir.glob("*.md"))
    print(f"📄 文件数量: {len(files)}")
    
    for file in files:
        size = file.stat().st_size
        print(f"  - {file.name}: {size} 字节")
    
    return True

def main():
    """主函数"""
    print("🏛️ h_k_mem - 分层记忆宫殿架构初始化工具")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "init":
            create_memory_palace()
        elif command == "check":
            check_memory_palace()
        elif command == "help":
            print("使用方法:")
            print("  python init_memory_palace.py init    # 初始化记忆宫殿")
            print("  python init_memory_palace.py check   # 检查记忆宫殿状态")
            print("  python init_memory_palace.py help    # 显示帮助")
        else:
            print(f"未知命令: {command}")
            print("使用 'help' 查看可用命令")
    else:
        # 默认初始化
        create_memory_palace()

if __name__ == "__main__":
    main()
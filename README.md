# rpmbuild

**COPR：** `https://copr.fedorainfracloud.org/coprs/biyuan/software/`

## 安装

```bash
sudo dnf copr enable biyuan/software
sudo dnf install <package>
```

## 仓库结构

```text
specs/                  # 各包 .spec
assets/<pkg>/           # 图标、LICENSE 等（spec 通过 raw.githubusercontent 引用）
  bilibili/
  hmcl/
  kazumi/
  splayer/
  splayer-next/
  hellwal/
  ...
```

## 已打包程序

| 包名 | 版本 | 说明 |
| --- | --- | --- |
| kazumi | 2.4.4 | 二次元追番 |
| hmcl | 3.16.4 | Minecraft 启动器 |
| bilibili | 1.20.0 | Bilibili 客户端 |
| miyu | 0.7.4 | 终端 AI 助手 |
| splayer | 3.1.1 | 音乐播放器 |
| splayer-next | 1.2.0 | 音乐播放器 |
| rime-ice | 2026.11.11 | 雾凇拼音 |
| grub-btrfs | 4.14 | GRUB Btrfs 快照 |
| waypaper | 2.9 | 壁纸管理器 |
| wpets-bongocat | 5.0.2 | 键盘跟手猫咪挂件 |
| hellwal | 1.0.9 | 终端取色 |
| kde-material-you-colors | 2.2.0 | KDE Material You |
| fcitx5-hud-paper | 1.0 | 自制 Hud Paper 主题（浅/深） |
| biyuan-niri-config | 20260922 | niri 桌面配置模板+部署脚本 |
| hyprwayland-scanner | 0.4.6 | wayland-scanner C++ 版（构建工具） |
| hyprutils | 0.14.3 | Hyprland C++ 基础库 |
| hyprlang | 0.6.8 | Hyprland 配置语言库 |
| hyprgraphics | 0.6.0 | Hyprland 图像加载库 |
| hypridle | 0.1.8 | Hyprland 闲置守护进程 |
| hyprlock | 0.9.7 | Hyprland 锁屏 |
| hyprpicker | 0.4.8 | Hyprland 取色器 |
| hyprland-protocols | 0.8.0 | Hyprland Wayland 协议扩展 |
| jetbrainsmono-nerd-fonts | 3.5.1 | JetBrainsMono 图标字体 |
| python3-materialyoucolor | 3.0.4 | Material You 纯 Python 算法库 |
| python3-screeninfo | 0.8.1 | 屏幕信息查询库 |
| python3-imageio-ffmpeg | 0.8.1 | Python FFmpeg 封装（含静态二进制） |
| sarasa-gothic-fonts | 1.0.43 | 更纱黑体 CJK 编程字体 |
| awww | 0.12.1 | Wayland 动态壁纸守护进程 |
| starship | 1.27.0 | 极简快速的 shell 提示符 |
| workbuddy | 5.6.2 | AI Agent 桌面应用 |
| lxgw-wenkai | 1.530 | 霞鹜文楷 CJK 字体（常规+等宽） |
| sarasa-mono-fonts | 1.0.43 | 更纱等宽 SC（+j/k/tc/hc/cl 子包） |
| sarasa-term-fonts | 1.0.43 | 更纱终端 SC（+j/k/tc/hc/cl 子包） |
| sarasa-all-fonts | 1.0.43 | 更纱全集单文件完整包 |
| maple-mono-nf-cn | 7.9 | Maple 代码字体中文图标版 |
| iosevka-term-nerd-fonts | 3.5.1 | Iosevka 终端图标字体（81 字形） |
| iosevka-nerd-fonts | 3.5.1 | Iosevka 标准图标字体（81 字形） |
| flclash | 0.9.3 | 跨平台代理客户端 |
| linglong-store | 3.7.0 | 玲珑应用商店社区版 |
| lazycat-terminal | 1.1.12 | Hackable 终端模拟器（标签页/分屏/透明背景） |
| gpu-screen-recorder | 6.1.7 | ShadowPlay 式 GPU 录屏 |
| ab-download-manager | 1.11.1 | 多线程下载管理器 |
| babry | 0.2.1 | Wayland 智能选区截图 |
| com.cmic.mcloud | 1.1.2 | 中国移动云盘桌面客户端 |
| escrcpy | 3.3.1 | scrcpy 图形界面客户端 |
| fcitx5-wetypex | 3.0.1.684 | WeTypeX 输入法（微信输入法 Linux 适配） |
| localsend | 1.18.2 | 开源跨平台隔空投送替代 |
| obsidian | 1.15.1 | 本地 Markdown 知识库 |
| python3-fast-colorthief | 0.0.5 | 图片主色提取 |
| python3-pywal16 | 3.8.15 | 配色方案生成切换 |
| wps-office | 12.1.2.29183 | WPS Office 办公套件 |

## 许可

各包遵循上游许可，spec 采用 MIT。

# import matplotlib.pyplot as plt
# from matplotlib.lines import Line2D
# from matplotlib.patches import Patch
# import numpy as np
# from PIL import Image
# from io import BytesIO
# import os

# def generate_strategy_legend_standalone():
#     """
#     Generates a standalone matplotlib figure containing only a custom horizontal legend
#     for the defined strategies and training types, mimicking a colorbar.
#     """
#     try:
#         # Define the strategies and train types as in your original code
#         strategies = [
#             "offline_3dgs_pcd", "offline_3dgs_gs", "offline_2dgs_pcd"
#         ]
#         train_types = [
#             "iter_0", "w_depth", "wo_depth"
#         ]

#         # Define color mapping - using more distinct colors
#         colors = {
#             "offline_3dgs_pcd": {"train": "lightblue", "test": "blue"},
#             "offline_3dgs_gs": {"train": "lightgreen", "test": "green"},
#             "offline_2dgs_pcd": {"train": "orange", "test": "red"}
#         }

#         # Set matplotlib parameters for clarity and readability (applied to the legend figure)
#         plt.rcParams['figure.dpi'] = 500
#         plt.rcParams['font.size'] = 12
#         plt.rcParams['axes.linewidth'] = 1.5
#         plt.rcParams['grid.linewidth'] = 0.8
#         plt.rcParams['lines.linewidth'] = 2.5
#         plt.rcParams['axes.titlesize'] = 14
#         plt.rcParams['axes.labelsize'] = 12

#         # Create a blank figure to host only the legend
#         fig_legend = plt.figure(figsize=(12, 3)) # Adjusted size for a horizontal legend
#         ax_legend = fig_legend.add_subplot(111)

#         # Hide the axes as we only want the legend
#         ax_legend.set_axis_off()

#         # Create handles and labels for the custom legend
#         custom_legend_handles = []
#         custom_legend_labels = []

#         # Define the desired order for legend entries
#         legend_order_templates = [
#             "{strategy} wo_depth (Train)",
#             "{strategy} wo_depth (Test)",
#             "{strategy} w_depth (Train)",
#             "{strategy} w_depth (Test)"
#         ]
#         full_legend_order = []
#         for strat in strategies:
#             for template in legend_order_templates:
#                 full_legend_order.append(template.format(strategy=strat))

#         # Add strategy/train_type entries
#         added_labels = set()
#         for strategy in strategies:
#             # wo_depth (solid line)
#             train_label_wo = f"{strategy} wo_depth (Train)"
#             test_label_wo = f"{strategy} wo_depth (Test)"

#             if train_label_wo not in added_labels:
#                 custom_legend_handles.append(Line2D([0], [0], color=colors[strategy]["train"], linestyle='-', linewidth=2.5))
#                 custom_legend_labels.append(train_label_wo)
#                 added_labels.add(train_label_wo)

#             if test_label_wo not in added_labels:
#                 custom_legend_handles.append(Line2D([0], [0], color=colors[strategy]["test"], linestyle='-', linewidth=2.5))
#                 custom_legend_labels.append(test_label_wo)
#                 added_labels.add(test_label_wo)

#             # w_depth (dashed line)
#             train_label_w = f"{strategy} w_depth (Train)"
#             test_label_w = f"{strategy} w_depth (Test)"

#             if train_label_w not in added_labels:
#                 custom_legend_handles.append(Line2D([0], [0], color=colors[strategy]["train"], linestyle='--', linewidth=2.5))
#                 custom_legend_labels.append(train_label_w)
#                 added_labels.add(train_label_w)

#             if test_label_w not in added_labels:
#                 custom_legend_handles.append(Line2D([0], [0], color=colors[strategy]["test"], linestyle='--', linewidth=2.5))
#                 custom_legend_labels.append(test_label_w)
#                 added_labels.add(test_label_w)

#         # Add the 'online' marker legend entries explicitly
#         # Assuming 'online' is represented by 'iter_0' from 'offline_3dgs_gs' strategy
#         custom_legend_handles.append(Line2D([0], [0], color='gray', marker='x', markersize=10, linestyle='None'))
#         custom_legend_labels.append('online (Train)')
#         custom_legend_handles.append(Line2D([0], [0], color='black', marker='x', markersize=10, linestyle='None'))
#         custom_legend_labels.append('online (Test)')

#         # Create sorted lists for handles and labels based on full_legend_order
#         sorted_handles = []
#         sorted_labels = []
#         # First, add the ordered strategy/train_type entries
#         for ordered_label in full_legend_order:
#             try:
#                 idx = custom_legend_labels.index(ordered_label)
#                 sorted_handles.append(custom_legend_handles[idx])
#                 sorted_labels.append(custom_legend_labels[idx])
#             except ValueError:
#                 pass # Label might not have been created if no data was assumed

#         # Then, append the 'online' markers
#         # Assuming 'online (Train)' and 'online (Test)' are always present in custom_legend_labels
#         online_train_idx = custom_legend_labels.index('online (Train)')
#         sorted_handles.append(custom_legend_handles[online_train_idx])
#         sorted_labels.append(custom_legend_labels[online_train_idx])

#         online_test_idx = custom_legend_labels.index('online (Test)')
#         sorted_handles.append(custom_legend_handles[online_test_idx])
#         sorted_labels.append(custom_legend_labels[online_test_idx])


#         # Create the legend and place it in the center of the blank figure
#         # Use a higher ncol to make it more horizontal
#         legend = ax_legend.legend(sorted_handles, sorted_labels, loc='center',
#                                   ncol=4,  # Adjust number of columns for horizontal layout
#                                   fontsize=12, frameon=True, fancybox=True, shadow=True)

#         # Adjust tight layout to fit the legend
#         fig_legend.tight_layout()

#         # Save the legend as an image
#         output_filename = "strategy_legend_colorbar_like.png"
#         plt.savefig(output_filename, format='png', dpi=500, bbox_inches='tight', pad_inches=0.1)
#         plt.close(fig_legend)

#         print(f"Generated standalone horizontal legend: {output_filename}")
#         return True

#     except Exception as e:
#         print(f"Failed to generate legend: {str(e)}")
#         import traceback
#         print(traceback.format_exc())
#         return False

# if __name__ == "__main__":
#     generate_strategy_legend_standalone()


import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from PIL import Image
from io import BytesIO
import os

def generate_strategy_legend_standalone_chinese():
    """
    生成一个独立的matplotlib图表，仅包含自定义的横向图例，
    用于展示不同策略和训练类型的颜色与线型，模拟“色条”效果。
    所有标注均使用中文。
    """
    try:
        # 定义策略和训练类型
        strategies = [
            "offline_3dgs_pcd", "offline_3dgs_gs", "offline_2dgs_pcd"
        ]
        train_types = [
            "iter_0", "w_depth", "wo_depth"
        ]

        # 定义颜色映射 - 使用更鲜明的颜色
        colors = {
            "offline_3dgs_pcd": {"train": "lightblue", "test": "blue"},
            "offline_3dgs_gs": {"train": "lightgreen", "test": "green"},
            "offline_2dgs_pcd": {"train": "orange", "test": "red"}
        }

        # 设置matplotlib参数以提高清晰度和可读性
        plt.rcParams['figure.dpi'] = 500  # 提高DPI
        plt.rcParams['font.size'] = 12    # 增大字体
        plt.rcParams['axes.linewidth'] = 1.5 # 增加轴线宽度
        plt.rcParams['grid.linewidth'] = 0.8 # 增加网格线宽度
        plt.rcParams['lines.linewidth'] = 2.5 # 增加曲线宽度
        plt.rcParams['axes.titlesize'] = 14 # 增大标题字体
        plt.rcParams['axes.labelsize'] = 12 # 增大轴标签字体

        # 尝试设置中文字体，确保中文能正常显示
        # 请根据你的系统安装的字体进行调整
        # 例如：'SimHei', 'Microsoft YaHei', 'Noto Sans CJK SC'
        try:
            plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Noto Sans CJK SC', 'Arial Unicode MS']
            plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题
        except Exception as e:
            print(f"警告：无法设置中文字体，图例可能显示乱码。错误信息: {e}")
            print("请确保你的系统中安装了中文字体，并在代码中指定正确的字体名称。")

        # 创建一个空白图表，专门用于放置图例
        fig_legend = plt.figure(figsize=(12, 3)) # 调整图表尺寸以适应横向图例
        ax_legend = fig_legend.add_subplot(111)

        # 隐藏坐标轴，因为我们只需要图例
        ax_legend.set_axis_off()

        # 为自定义图例创建句柄和标签
        custom_legend_handles = []
        custom_legend_labels = []

        # 定义图例项的理想顺序
        legend_order_templates = [
            "{strategy_cn} 无深度 (训练)",
            "{strategy_cn} 无深度 (测试)",
            "{strategy_cn} 有深度 (训练)",
            "{strategy_cn} 有深度 (测试)"
        ]

        # 策略名称的中文映射
        strategy_chinese_names = {
            "offline_3dgs_pcd": "离线3DGS-点云",
            "offline_3dgs_gs": "离线3DGS-高斯",
            "offline_2dgs_pcd": "离线2DGS-点云"
        }

        full_legend_order = []
        for strat in strategies:
            strategy_cn = strategy_chinese_names.get(strat, strat) # 获取中文名
            for template in legend_order_templates:
                full_legend_order.append(template.format(strategy_cn=strategy_cn))

        # 添加策略/训练类型条目
        added_labels = set()
        for strategy in strategies:
            strategy_cn = strategy_chinese_names.get(strategy, strategy)

            # 无深度 (实线)
            train_label_wo = f"{strategy_cn} 无深度 (训练)"
            test_label_wo = f"{strategy_cn} 无深度 (测试)"

            if train_label_wo not in added_labels:
                custom_legend_handles.append(Line2D([0], [0], color=colors[strategy]["train"], linestyle='-', linewidth=2.5))
                custom_legend_labels.append(train_label_wo)
                added_labels.add(train_label_wo)

            if test_label_wo not in added_labels:
                custom_legend_handles.append(Line2D([0], [0], color=colors[strategy]["test"], linestyle='-', linewidth=2.5))
                custom_legend_labels.append(test_label_wo)
                added_labels.add(test_label_wo)

            # 有深度 (虚线)
            train_label_w = f"{strategy_cn} 有深度 (训练)"
            test_label_w = f"{strategy_cn} 有深度 (测试)"

            if train_label_w not in added_labels:
                custom_legend_handles.append(Line2D([0], [0], color=colors[strategy]["train"], linestyle='--', linewidth=2.5))
                custom_legend_labels.append(train_label_w)
                added_labels.add(train_label_w)

            if test_label_w not in added_labels:
                custom_legend_handles.append(Line2D([0], [0], color=colors[strategy]["test"], linestyle='--', linewidth=2.5))
                custom_legend_labels.append(test_label_w)
                added_labels.add(test_label_w)

        # 明确添加“online”标记的图例项
        custom_legend_handles.append(Line2D([0], [0], color='gray', marker='x', markersize=10, linestyle='None'))
        custom_legend_labels.append('在线 (训练)')
        custom_legend_handles.append(Line2D([0], [0], color='black', marker='x', markersize=10, linestyle='None'))
        custom_legend_labels.append('在线 (测试)')

        # 根据 full_legend_order 创建排序后的句柄和标签列表
        sorted_handles = []
        sorted_labels = []
        # 首先添加排序后的策略/训练类型条目
        for ordered_label in full_legend_order:
            try:
                idx = custom_legend_labels.index(ordered_label)
                sorted_handles.append(custom_legend_handles[idx])
                sorted_labels.append(custom_legend_labels[idx])
            except ValueError:
                pass # 忽略未创建的标签

        # 然后，追加“在线”标记
        # 假设“在线 (训练)”和“在线 (测试)”总会出现在 custom_legend_labels 中
        online_train_idx = custom_legend_labels.index('在线 (训练)')
        sorted_handles.append(custom_legend_handles[online_train_idx])
        sorted_labels.append(custom_legend_labels[online_train_idx])

        online_test_idx = custom_legend_labels.index('在线 (测试)')
        sorted_handles.append(custom_legend_handles[online_test_idx])
        sorted_labels.append(custom_legend_labels[online_test_idx])

        # 创建图例并将其放置在空白图表的中心
        # 增加 ncol 使其更水平
        legend = ax_legend.legend(sorted_handles, sorted_labels, loc='center',
                                  ncol=4,  # 根据需要调整列数以获得更好的横向布局
                                  fontsize=12, frameon=True, fancybox=True, shadow=True)

        # 调整布局以适应图例
        fig_legend.tight_layout()

        # 将图例保存为图片文件
        output_filename = "策略图例_中文.png"
        plt.savefig(output_filename, format='png', dpi=500, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig_legend)

        print(f"已生成独立的中文横向图例文件: {output_filename}")
        return True

    except Exception as e:
        print(f"生成图例失败: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return False

if __name__ == "__main__":
    generate_strategy_legend_standalone_chinese()
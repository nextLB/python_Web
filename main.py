import cv2
from ultralytics import YOLO
import time
import os


def save_detection_video():
    """
    将检测结果保存为视频文件
    """
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("错误：无法访问摄像头")
        return

    # 获取摄像头帧的宽度和高度
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20.0  # 帧率

    # 创建保存结果的目录
    output_dir = "detection_results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 创建视频编写器
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    video_filename = f"{output_dir}/detection_{timestamp}.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4编码
    out = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))

    print("YOLO人体检测已启动，结果将保存为视频")
    print(f"视频保存路径: {video_filename}")
    print("按 Ctrl+C 退出程序")

    frame_count = 0
    start_time = time.time()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("错误：无法读取摄像头帧")
                break

            frame_count += 1

            # 使用YOLO进行推理
            results = model(frame, classes=[0], conf=0.5)

            # 获取检测结果
            person_count = len(results[0].boxes)

            # 绘制检测结果
            annotated_frame = results[0].plot()

            # 在帧上添加文本信息
            cv2.putText(annotated_frame, f"Persons: {person_count}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(annotated_frame, f"Time: {time.strftime('%H:%M:%S')}", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(annotated_frame, f"Frame: {frame_count}", (10, 110),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # 将帧写入视频文件
            out.write(annotated_frame)

            # 输出当前状态
            elapsed_time = time.time() - start_time
            status = f"帧: {frame_count}, 检测到人数: {person_count}, 录制时间: {elapsed_time:.1f}秒"
            print(status, end='\r')

    except KeyboardInterrupt:
        print("\n程序被用户中断")
    finally:
        # 释放资源
        cap.release()
        out.release()

        # 计算总录制时间
        total_time = time.time() - start_time
        print(f"\n程序已退出，视频保存为: {video_filename}")
        print(f"总录制时间: {total_time:.2f}秒")
        print(f"总帧数: {frame_count}")
        print(f"平均帧率: {frame_count / total_time:.2f} FPS")


if __name__ == "__main__":
    save_detection_video()
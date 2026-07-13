'''
시현
 

'''

import os
import cv2
import argparse
import time

def process_video(input_path, output_path):
    #open input video
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print(f"Unable to open video file from spcified path: {input_path}")
        return
    
    #read video properties and display on terminal
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    print(f"Frame width: {frame_width}")
    print(f"Frame height: {frame_height}")
    print(f"Frames per second: {fps}")

    #만약 사용자가 지정한 디렉터리가 없으면 만들어줘야하므로 파일총경로에서 디렉터리경로만 추출
    output_dir = os.path.dirname(output_path)
    #만약 output_path가 processed.mp4 처럼 파일경로 없으면 output_dir = ""되기때문에 makedirs에서 유효경로가아니게되서 if문 추가해줌
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Create output video writer
    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (frame_width, frame_height)
    )

    frame_count = 0
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        #프레임 처리 성공하면 +1
        frame_count+=1

        #Frame number overlay
        cv2.putText(
            frame,
            f"Frame: {frame_count}", #몇번째 프레임 처리인지 화면에 오버레이로 표시
            (30,50), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            (0,255,0), #색상 BGR순서
            2, #글자두께
            cv2.LINE_AA #선 처리 방식
        )

        #원본 비디오 프레임
        cv2.putText(
            frame,
            f"Video FPS: {fps:.2f}",
            (30, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

        out.write(frame)

    end_time = time.time()
    elapsed_time = end_time - start_time

    processing_fps = frame_count / elapsed_time

    cap.release()
    out.release()

    print(f"Frames processed: {frame_count}")
    print(f"Processing FPS: {processing_fps:.2f}")

def main():
    #argparse 객체 생성
    parser = argparse.ArgumentParser(description="Video Frame Processor")

    #명령줄 parameter 추가
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input video file"
    )

    #명령줄 parameter 추가
    parser.add_argument(
        "--output",
        required=True,
        help="Path to the output video file"
    )

    #명령줄 parameters 파싱
    args = parser.parse_args()

    #사용
    process_video(args.input, args.output)

if __name__ == "__main__":
    main()
## 작업	명령어

- 파일 업로드	`hdfs dfs -put <로컬경로> <HDFS경로>`
파일 다운로드	`hdfs dfs -get <HDFS경로> <로컬경로>`
파일 목록 보기	`hdfs dfs -ls /경로`
파일 삭제	hdfs dfs -rm /경로/파일
폴더 삭제	hdfs dfs -rm -r /경로
폴더 생성	hdfs dfs -mkdir /경로
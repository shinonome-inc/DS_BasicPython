# DataScienceコース 課題リポジトリ
DataScienceコースの課題提出に使うリポジトリです。  
実際の課題の進め方は下記を参照してください。

## 課題開始前のセットアップ

1. 個人でリポジトリを作成する。  
  1.1.このページの右上のUse This Templateをクリック  
  <img width="287" alt="スクリーンショット 2022-04-04 10 43 57" src="https://user-images.githubusercontent.com/70427875/161460844-add34447-42c7-40c2-9b2e-d662e24eef34.png">
  1.2.Ownerを自分（あなた）に変更し、Publicでリポジトリを作成する(include all branchesにはチェック入れない)  
  <img width="761" alt="スクリーンショット 2022-04-04 10 46 24" src="https://user-images.githubusercontent.com/70427875/161460958-acb2c2e8-edde-44d9-bc76-3e05a24cbf5b.png"><br>

2. 作成したリポジトリをクローンする。

3. ローカルで下記コマンドを実行し、課題に必要なモジュールをインストールしておく。
  ```shell
  pip install -r requirements.txt
  ```

## 課題の進め方
教材と課題が[こちら](https://shinonome.io/PythonTutorialForDSCourse)にまとまっています。 
受講生の皆さんは下記の手順で課題を進めてください
1. 読み物を読む  
2. 直後に確認問題があればそれを解く  
   - このとき、該当の確認課題を実装するためのブランチをつくり、そこで作業してください。
   - 確認課題はトピックごと数問の小問から構成されていますが、ブランチは**トピックごとに**作成してください。（小問ごとではありません）
3. 提出する  
  3.1 実装した内容をgithub上の対応するブランチにプッシュする  
  3.2 実装したブランチから`main`へのプルリクエストを作成する  
  3.3 プルリクエストのリンクをレビュワーに送信する  

## 各課題のレビュワー
|課題|レビュワー|
|:-:|:-:|
|Python入門|yuto|
|制御構文|kobakoba|
|関数|Ryuichi|
|numpy|tomoya|
|pandas|takeshun|
|matplotlib|Taichi(Ando)|
|scikit-learn|Taichi(Ando)|

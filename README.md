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
|pandas|Ryoji|
|matplotlib|Ryoma|
|scikit-learn|shima|

# ※注意※コード規約について

課題を提出をするときは、

- コードがコード規約に従っている（PEP8）
- python3で解いている
- 実際に実行し、想定通りの出力が出ている

ということを必ず確認してから提出するようにしてください。

<aside>
💡 **コード規約**

[PEP8](https://pep8-ja.readthedocs.io/ja/latest/)とは、Pythonにおけるスタイルガイドのこと。

スタイルガイドとは、変数や関数名の付け方、空白に関する内容や、インデントの仕方、コメントの書き方など様々な基本的なルールを定義しているもの。

実際の開発では複数人で作業することが一般的である。その際にコード規約に従うことでコードに一貫性が生まれ、可読性・保守性が高まり品質の向上につながる。

</aside>
このサイトで自分のコードがコード規約に従っているかチェックすることができます。(https://www.pythonchecker.com/)

### vscodeのsettings.jsonを編集してコード規約を自動的に守る方法

下のsettings.jsonファイルをダウンロードして.vscode直下に置いてください。(GitHubからリポジトリをクローンすれば、自動的にvscode直下に置かれます。)自動で保存時にコード規約に従ったコードへと変換されます。詳しくは[こちら](https://maku.blog/p/tfq2cnw/)。

black, flake8をインストールしていないとvscodeで警告が出るので自身の環境にあわせて(conda or pip)インストールしてください。↓
<img width="450" alt="スクリーンショット 2022-04-04 0 24 03" src="https://user-images.githubusercontent.com/70427875/161435394-b5018694-aee2-4a89-813d-9cfa4e9b7c15.png">


わからないことがあればslackで@eriにお願いします。

↓GitHubからクローンしてもvscode直下に置かれなかった方用<br>
[settings.json.zip](https://github.com/shinonome-inc/Basic-Python/files/8357521/settings.json.zip)


<img width="287" alt="スクリーンショット 2022-03-20 19 31 34" src="https://user-images.githubusercontent.com/83397726/160279459-afeb9b5e-cfb1-4aa3-b26d-1e1433ae816e.png">


（フォーマッターを使わない方は[こちら](https://atmarkit.itmedia.co.jp/ait/articles/1912/10/news045.html)を参考にしてください。）

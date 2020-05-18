# how to use

***************************


## 1, color_creator.pyの実行(単色画像をたくさんつくります)
新規フォルダを作成し、画像を保存します。<br>
csvファイルを新規作成し、各画像のr,g,bの各値のデータを保存します。<br>
★プログラム実行後のサンプルとして、colorsフォルダ、created_colors.csvが既に用意されています。
|colorsフォルダ|created_colors.csv|
|---|---|
|<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/287b773d-c661-67f3-6509-9c3902e305e8.png" width="300">|<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/230502e4-f611-9c03-43ec-938e4b978802.png" width="300">|




## 2, color_teacher.pyの実行（単色画像にラベルをつけます）
1で作成したcsvファイルからランダムにn件のデータを選択し、GUIによってラベルをつけます。<br>
csvファイルを新規作成し、作成したデータを保存します。<br>
★プログラム実行後のサンプルとして、既にlearned_colors_green.csv、learned_colors_myfavorites.csvが用意されています。<br>
→learned_colors_green.csvは、緑色とその他の色を分類しています。learned_colors_myfavorites.csvは、私の好きな色と好きでない色とを分類しています。<br>
★デフォルトでは、n=300です。あまり大きな数にすると、学習データを作るのが大変になります。教師はあなたです。<br>
|Mr. 1 or 0|learned_colors_green.csv|
|---|---|
|<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/92b2bbbc-2d8a-491e-5e09-5e8b4e9715b2.png" width="300">|<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/78c96ad9-fc43-9aa7-aeca-6a73ad7101b6.png" width="300">|

## 3, graph_display.pyの実行（3次元プロットします）
2で作成したラベルの貼られたcsvファイルを読み込み、3次元プロットを作成します。データを直感的に分析することができます。<br>
★サンプルとして用意されたlearned_colors_green.csv、learned_colors_myfavorites.csvをすぐに読み込むことができます。<br>
|learned_colors_green.csv|
|---|
|<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/9708e565-74f3-8c97-4999-eef7e1a1c5fb.png" width="450">|


## 4, predict_LogisticRegression.py、またはpredict_DecisionTree.pyの実行（予測を行ないます）
2で作成したcsvファイルを読み込み、学習済みデータを任意の割合（デフォルトでは7:3）でトレーニング用とテスト用に分けます。トレーニング用データで学習学習を行ないます。学習後、テスト用データで学習の成果の検証を行ないます。<br>
★predict_LogisticRegression.pyではロジスティック回帰分析を使用します。ROC曲線のグラフを表示します。<br>
★predict_DecisionTree.pyでは決定木を使用します。<br>

learned_colors_green.csv（緑色かその他の色か）
|predict_LogisticRegression.py|predict_DecisionTree.py|
|---|---|
|![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/c3f7d9ca-d931-683f-28f2-265b43d0d2dd.png)|![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/56a55123-d6b4-c85a-947a-cf9ccb04658d.png)|

learned_colors_myfavorites.csv（私の好きな色か、そうでない色か）
|predict_LogisticRegression.py|predict_DecisionTree.py|
|---|---|
|![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/85c52b81-79bb-8706-12bf-587086ffe2d6.png)|![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/5006f865-614d-0864-fe84-c53010faa5a3.png)|

|predict_LogisticRegression.py(learned_colors_myfavorites.csv)|
|---|
|<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/579786/df36eec2-ad74-e8a1-c066-48652335aced.png" width="450">|
****************************

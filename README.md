# how to use

***************************


## 1, color_creator.pyの実行(単色画像をたくさんつくります)
新規フォルダを作成し、画像を保存します。<br>
csvファイルを新規作成し、各画像のr,g,bの各値のデータを保存します。<br>
★プログラム実行後のサンプルとして、colorsフォルダ、created_colors.csvが既に用意されています。


## 2, color_teacher.pyの実行（単色画像にラベルをつけます）
1で作成したcsvファイルからランダムにn件のデータを選択し、GUIによってラベルをつけます。<br>
csvファイルを新規作成し、作成したデータを保存します。<br>
★プログラム実行後のサンプルとして、既にlearned_colors_green.csv、learned_colors_myfavorites.csvが用意されています。<br>
→learned_colors_green.csvは、緑色とその他の色を分類しています。learned_colors_myfavorites.csvは、私(うぃるこむ)の好きな色と好きでない色とを分類しています（あくまでも個人的な趣向です）。<br>
★デフォルトでは、n=300です。あまり大きな数にすると、学習データを作るのが大変になります。教師はあなたです。<br>


## 3, graph_display.pyの実行（3次元プロットします）
2で作成した学習済みcsvファイルを読み込み、3次元プロットを作成します。データを直感的に分析することができます。<br>
★サンプルとして用意されたlearned_colors_green.csv、learned_colors_myfavorites.csvをすぐに読み込むことができます。<br>

## 4, predict_LogisticRegression.py、またはpredict_DecisionTree.pyの実行（予測を行ないます）
2で作成したcsvファイルを読み込み、学習済みデータを任意の割合（デフォルトでは7:3）でトレーニング用とテスト用に分けます。トレーニング用データで学習学習を行ないます。学習後、テスト用データで学習の成果の検証を行ないます。<br>
★predict_LogisticRegression.pyではロジスティック回帰分析を使用します。<br>
★predict_DecisionTree.pyでは決定木を使用します。<br>
****************************

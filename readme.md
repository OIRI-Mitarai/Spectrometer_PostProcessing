# 準備
## 1. 構成
以下の構成に揃える。<br>
作業用ディレクトリ<br>
　└ measument_plot.py<br>
　└ requirements.txt<br>
　└ data<br>
　　├ (業者保存ファイル名　※任意).txt<br>
　　├ (業者保存ファイル名　※任意).txt<br>
　　├ 　　…<br>
　　└ (業者保存ファイル名　※任意).txt<br>
## 2. 環境構成
以下、(a)または(b)の手順で構成をする。pythonライブラリは容量圧迫傾向にあるため(a)が推奨。実行後venvフォルダを削除することで一時的な利用で蓄積・圧迫しがちなpythonライブラリを捨てることが出来る。
- (a) 仮想環境構築<br>
　　エクスプローラ上部タブ フォルダパスに「cmd」を入力<br>
　　コマンドプロンプトへ以下入力
    ```
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
- (b) 素のpython環境にライブラリインストール<br>
　　エクスプローラ上部タブ フォルダパスに「cmd」を入力<br>
　　コマンドプロンプトへ以下入力
    ```
    pip install -r requirements.txt
    ```

# プロット描画
以下をコマンドプロンプトへ入力することで「Graph_plot.png」の画像ファイルが作業用フォルダに生成される。
```
python measument_plot.py
```
もし前手順で(a)を選んでいる場合は作業終了時に**作業用フォルダ内にある「venv」のフォルダを丸ごと消してよい。**

# txt→csv一括マージ
以下をコマンドプロンプトへ入力することで「merged_data.csv」のcsvファイルが作業用フォルダに生成される。
```
python merge_result_csv.py
```
もし前手順で(a)を選んでいる場合は作業終了時に**作業用フォルダ内にある「venv」のフォルダを丸ごと消してよい。**

# メンテナンスについて
## 1. python環境
pythonは3.6以降なら問題ない見込み。2.x(2.7など)が怪しい。<br>
参考まで、手元環境は3.12.3。
## 2. プロット描画スクリプト
修正対象は以下の見込み。
* txtデータ格納フォルダ<br>
「data」のフォルダ名としている。
    ```
    data_folder = 'data'
    ```
* エンコード・デコードエラー<br>
txtファイル記載の文字が読めないエラー。shift_jis・cp932・utf-8…などtxtファイルの文字コードに合わせて読み出しをしないとスクリプトが読み出せない。<br>
現状は「cp932」としている以下をshift_jisやutf-8など他の文字コードで試す。
    ```
    # load csv data
    df = pd.read_csv(file_path, encoding='cp932', skiprows=1)
    ```
* 保存ファイル名<br>
「Graph_plot.png」としている。他のものにする場合は以下を修正。
    ```
    # save plot
    plt.savefig('Graph_plot.png')
    ```

## 3. csvマージスクリプト
修正対象は以下の見込み。
* txtデータ格納フォルダ<br>
「data」のフォルダ名としている。
    ```
    data_folder = 'data'
    ```
* エンコード・デコードエラー<br>
txtファイル記載の文字が読めないエラー。shift_jis・cp932・utf-8…などtxtファイルの文字コードに合わせて読み出しをしないとスクリプトが読み出せない。<br>
現状は「cp932」としている以下をshift_jisやutf-8など他の文字コードで試す。
    ```
    # skip 1st row
    df = pd.read_csv(file_path, encoding='cp932', skiprows=1)
    ```
* 保存ファイル名<br>
「merged_data.csv」としている。他のものにする場合は以下を修正。
    ```
    # save
    merged_df.to_csv('merged_data.csv', index=False, encoding='utf-8-sig')
    ```

# 送付メールについて
## 1. メール文面(例)
```
株式会社 xx　○○様

大分県産業科学技術センターの○○と申します。
いつもお世話になっております。

本日は分光光度計のご利用、ありがとうございました。
測定データを添付ファイルにてお送りいたしますので、ご確認ください。
ご不明点やご質問等がございましたら、お気軽にご連絡くださいませ。

以上、今後とも当センターをどうぞよろしくお願い致します。
```
## 2. 添付ファイル
* 分光光度計出力ファイル
* グラフプロットの画像ファイル
* txt→csvマージファイル<br>
* (※spcファイルも入れているが多分不要)
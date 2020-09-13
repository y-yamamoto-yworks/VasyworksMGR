1.Vasywoksについて
Vasyworks（ベイジーワークス）は賃貸管理業において、空室情報を登録、公開するための一連のシステムの総称です。主に賃貸管理業者（法人および個人）が管理物件の空室情報を賃貸仲介業者に公開するための利用を想定しています。

VasyworksはVasyworksDB（データベース構築プロジェクト）、VasyworksMGR（空室情報データ管理プロジェクト）、VasyworksLIST（空室情報一覧プロジェクト）、VasyworksAPI（空室情報APIプロジェクト）など複数のプロジェクトから構成されています。

2.VasyworksMGR（空室情報データ管理プロジェクト）について
VasyworksMGRはVasyworksの空室情報データ管理するためのプロジェクトです。VasyworksDBで構築されたデータベースを利用します。Vasyworksの空室情報の登録・変更・削除等にはVasyworksMGRを利用します。また、VasyworksLISTの閲覧ユーザの管理もVasyworksMGRで行います。

3.VasyworksMGRのライセンスについて
VasyworksMGRのソースコードは山本 泰弘の著作物として、AGLPv3のライセンス条件の下で利用できます。

4.動作環境について
開発環境は下記の通りです。
・OS: Ubuntu 18.04
・Nginx 1.14.0
・PostgreSQL10.14
・Python3.7 venv
・Django 2.2.14

5. インストールについて
VasyworksLISTのdocsディレクトリにある「格安サーバ構築.txt」を参照してください。

6. DEMO環境
VasyworksDB   http://vacancy.yworks.net:8080/admin/  （ログインユーザ情報非公開）
VasyworksMGR  http://vacancy.yworks.net:8081/        （ログインユーザ情報公開）
VasyworksLIST  http://vacancy.yworks.net/             （ログインユーザ情報公開）

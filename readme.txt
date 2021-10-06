1.Vasywoksについて
Vasyworks（ベイジーワークス）は賃貸管理業において、空室情報を登録、公開するための一連のシステムの総称です。主に賃貸管理業者（法人および個人）が管理物件の空室情報を賃貸仲介業者に公開するための利用を想定しています。

VasyworksはVasyworksDB（データベース構築プロジェクト）、VasyworksMGR（空室情報データ管理プロジェクト）、VasyworksLIST（空室情報一覧プロジェクト）、VasyworksAPI（空室情報APIプロジェクト）、VasyworksSEARCH（空室情報検索プロジェクト）など複数のプロジェクトから構成されています。

Vasyworks全般についての説明は、下記のURLのサイトを参照してください。

--
Vasyworks:無料で使えるオープンソースの賃貸空室情報システム【賃貸管理業者向け】
https://vasyworks.yworks.net
--

2.VasyworksMGR（空室情報データ管理プロジェクト）について
VasyworksMGRはVasyworksの空室情報データ管理するためのプロジェクトです。VasyworksDBで構築されたデータベースを利用します。Vasyworksの空室情報の登録・変更・削除等にはVasyworksMGRを利用します。また、VasyworksLISTの閲覧ユーザの管理もVasyworksMGRで行います。

3.VasyworksMGRのライセンスについて
VasyworksMGRのソースコードは山本 泰弘の著作物として、AGLPv3のライセンス条件の下で利用できます。

4.動作環境について
開発環境は下記の通りです。
・OS: Ubuntu 20.04
・Nginx 1.18.0
・PostgreSQL12.7
・Python3.8 venv
・Django 3.2.4

5. インストールについて
下記のURLを参照してください。
https://vasyworks.yworks.net/index.php/install/

6. DEMO環境
VasyworksDB   http://vasyworks-db.yworks.net:/admin/  （ログインユーザ情報非公開）
VasyworksMGR  http://vasyworks-mgr.yworks.net/        （ログインユーザ情報公開）
VasyworksLIST  http://vasyworks-list.yworks.net/             （ログインユーザ情報公開）
VasyworksAPI  http://vasyworks-api.yworks.net/             （ログイン不要）
VasyworksSEARCH  http://vasyworks-search.yworks.net/        （ログインユーザ情報公開）

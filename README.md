# backuper
## abstract
jsonで指定したディレクトリに、指定したサーバーのバックアップデータを作成するプログラムです。　　
scpを使用できる環境であれば使用できます

## 環境
```
Python 3.6.5 
```
python以外の追加ライブラリは必要ありません

## 使用方法
main.shと同階層に
```
dir_info.json
```
を作成し、以下のようにバックアップを保存するディレクトリ(save_dir)と、バックアップを撮りたいディレクトリ(bachup_list -> cliant)及び、サーバーのssh名を指定(cliant)してください。
```
{
    "save_dir":"/media/ryusei/strage/share/ryusei/backup",
    "backup_list":[
        {
            "cliant":"alan-dekabutu",
            "path":"/media/ryusei/wkdir/src/uma"
        }
    ]
}
```

その後、
```
main.sh
```
を実行すれば、バックアップが始まり、日時の名前がついたディレクトリにバックアップが保存されます。
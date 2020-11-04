import dataclasses


@dataclasses.dataclass(frozen=True)
class Strings:
    """テキストを置き換えます"""
    # common
    your_account_banned = ["あなたのアカウントはBANされています(´;ω;｀)\nBANに対する異議申し立ては、公式サーバーの <#{}> にてご対応させていただきます。", "Your account is banned (´; ω;`)\nIf you have an objection to BAN, please use the official server <#{}>.", "당신의 계정은 차단되어 있습니다 ( '; ω;`)\n차단에 대한 이의 신청은 공식 서버 <#{}> 에서 대응하겠습니다.", "Su cuenta está prohibida (´; ω;`)\nSi tiene una objeción a la BAN, utilice <#{}> en el servidor oficial."]
    missing_arguments = ["引数が不足しているよ!\n使い方: `{0}{1}`\n詳しくは `{0}help {2}`", "Not enough arguments! \nUsage: `{0}help {1}` \nFor more information `{0}help {2}", "f 인수가 충분하지 않습니다. \n사용법 :`{0} {1}`\n 자세한 내용은`{0}help {2}", "No hay suficientes argumentos. \nUso: {0} {1} \nPara obtener más información, `{0}help {2}"]
    interval_too_fast = ["コマンド実行の間隔が速すぎるよ! `{:.2f}`秒後に再度使用できるよ!", "The command execution interval is too fast! You can use it again in `{:.2f}` seconds!", "명령 실행 간격이 너무 빠릅니다! `{:.2f}` 초 후에 다시 사용할 수 있습니다!", "¡El intervalo de ejecución del comando es demasiado rápido! ¡Puede volver a utilizarlo en `{:.2f}` segundos!"]
    error_occurred = ["エラーが発生しました。管理者にお尋ねください。\n{}", "An error has occurred. Please ask the BOT administrator.\n{}", "오류가 발생했습니다.관리자에게 문의하십시오.\n{}", "Se ha producido un error. Pregunte al administrador.\n{}"]
    missing_subcommand = ["サブコマンドが不足しているよ!\n`{0}help add`で使い方を確認してね!", "Missing subcommands!\n`{0}help add` to see how to use it!", "하위 명령이 부족한거야! \n`{0}help add` 사용법을 확인 해!", "¡Faltan subcomandos! \n`{0}help add` para ver cómo se usa!"]
    # main.py
    prefix_of_the_bot = ["このBOTのprefixは`{}`です!\n`{}help`で詳しい使い方を確認できます。", "The prefix for this bot is `{}`! \n`{}help` for more details on how to use it.", "이 봇의 접두사는`{}`입니다! 사용 방법에 대한 자세한 내용은 \n` {} 도움말`을 참조하세요.", "¡El prefijo de este bot es `{}`! \n`{}help` para obtener más detalles sobre cómo usarlo."]
    # costume.py
    welcome_to_costume_title = ["装飾シミュレータへようこそ!", "Welcome to the costume simulator!", "코스튬 시뮬레이터에 오신 것을 환영합니다!", "¡Bienvenido al simulador de disfraz!"]
    welcome_to_costume_description = [
        "装飾シミュレータ操作用コマンドのリストは`{0}help Costume`で確認できるよ!\nm!add (base/character/weapon/head/body/back) 番号 \nm!list (base/character/weapon/head/body/back)\n例:\n`{0}list character`\n`{0}add character 1`\n実際に上の例にあるコマンドを使ってみてね！\nもっと知りたいって人はこの動画を見てね！\n[https://www.youtube.com/watch?v=WgZ83Dt955s](https://www.youtube.com/watch?v=WgZ83Dt955s)",
        "Welcome to the costume simulator!\nYou can see the list of commands for operating the costume simulator with `{0}help Costume`!\n{0}add (base / character / weapon / head / body / back) number\n{0}list (base / character / weapon / head / body / back)\nExample:\n`{0}list character`\n`{0}add character 1`\nTry using the command in the example above to understand!",
        "코스튬 시뮬레이터에 오신 것을 환영합니다!\n코스튬 시뮬레이터 조작 명령어는 `{0}help Costume`에서 확인 할 수 있어!\n{0}add (base / character / weapon / head / body / back) 번호\n{0}list (base / character / weapon / head / body / back)\n예 :\n`{0}list character`\n`{0}add character 1`\n실제로 위의 예제에있는 명령을 사용 해보세요!\n더 알고 싶은 사람은 동영상을 보세요!\n[https://www.youtube.com/watch?v=WgZ83Dt955s](https://www.youtube.com/watch?v=WgZ83Dt955s)",
        "¡Bienvenido al simulador de disfraz!\n¡Puedes ver la lista de comandos para operar el simulador de disfraz con `{0}help Costume`!\n{0}add (base / personaje / arma / cabeza / cuerpo / espalda) \n{0}list (base / personaje / arma / cabeza / cuerpo / espalda)\nEjemplo:\n`{0}list character`\n`{0}add character 1`\n¡Intente usar el comando del ejemplo anterior!"
    ]
    costume_table_base = ["ベース色", "base", "색상", "base"]
    costume_table_character = ["キャラクター", "character", "캐릭터", "caracteres"]
    costume_table_weapon = ["武器", "weapon", "무기", "arma"]
    costume_table_head = ["頭装飾", "head", "머리", "cabeza"]
    costume_table_body = ["体装飾", "body", "몸", "cuerpo"]
    costume_table_back = ["背中装飾", "back", "허리", "espalda"]
    costume_table_code = ["装飾コード: {}", "CostumeCode: {}", "장식 코드: {}", "código de decoración: {}"]
    no_th_saved_work = ["{}番目に保存された作品はないよ!", "There is no {}th saved work!", "{} 번째로 저장된 작품은 아니야!", "¡No hay {}th trabajo guardado!"]
    specify_between_1_20 = ["1~20の間で指定してね!.", "Please specify between 1 and 20 !.", "1 ~ 20 사이의 값을!.", "Por favor, especifique entre 1 y 20."]
    not_found_with_name = ["そのような名前の作品はないよ!", "There is no work with that name!", "그런 이름의 작품은 아니에요!", "¡No hay obra con tal nombre!"]
    loaded_work = ["{}番目の\"{}\"を読み込みました.", "loaded {}th {}", "{} 번째 \"{}\"을 읽어 습니다.", "{}th \"{}\" cargado"]
    save_up_to_20 = ["保存できるのは20個までだよ! 不要なものを削除してから保存してね!", "You can save up to 20! Delete unnecessary ones before saving!", "불필요한 것들은 빼고 20개까지 저장해줄거야!", "¡Puedes guardar hasta 20! ¡Elimina los innecesarios antes de guardar!"]
    int_only_name_not_allowed = ["数字のみの名前は使用できないよ!", "You can't use numbers-only names!", "숫자를 이름으로는 사용할 수 없어!", "¡No puedes usar nombres de solo números!"]
    name_already_used = ["この名前は既に他の作品についてるよ!.", "This name is already on other works !", "이 이름은 이미 다른 작품에 사용되었어요!", "¡Este nombre ya está en otros trabajos!"]
    name_length_between_1_20 = ["名称は1文字以上20文字以下で指定してね!", "Please specify the name with 1 to 20 characters!", "이름은 1 ~ 20자로 지정주세요!", "Por favor, especifique el nombre con 1 a 20 caracteres."]
    saved_work = ["保存したよ! 名称: '{}'", "Saved! Name: '{}'", "저장 했어! 이름: '{}'", "¡Guardado!. Nombre: '{}'"]
    page_number_between = ["ページ数は1~{}で指定してね!", "Specify the number of pages from 1 to {}!", "페이지 수는 1 ~ {} 중에서 지정주세요!", "¡Especifique el número de páginas de 1 a {}!"]
    page_number_integer_between = ["ページ数は整数で1~{}で指定してね!", "Specify the number of pages as an integer from 1 to {}!", "페이지 수는 정수 1 ~ {} 중에서 지정주세요!", "¡Especifique el número de páginas como un número entero de 1 a {}!"]
    my_title = ["保存した作品集 ({} / 4 ページ)", "Saved work collection ({} / 4 pages)", "저장된 작품집 ({} / 4 페이지)", "Colección de trabajos guardados ({} / 4 páginas)"]
    my_description = ["左の数字が保存番号、その横の名前が保存名称だよ!。その下の英数字6,7桁の文字列が装飾コードだよ!", "The number on the left is the save number, and the name next to it is the save name! The 6 or 7 alphanumeric character string below it is the decoration code!", "왼쪽의 숫자가 저장 명칭이야! 그 아래 숫자 6,7 자리는 코스튬 코드이야!",
                      "El número de la izquierda es el número de guardado, y el nombre al lado es el nombre de guardado. ¡La cadena de 6 o 7 dígitos debajo es el código de decoración!"
                      ]
    deleted_work = ["{}番目の{}を削除したよ!", "The {} th {} has been deleted!", "{} 번째 {}를 삭제 했어!", "¡El {} th {} ha sido eliminado!"]
    not_found_with_number = ["{}番目に保存された作品はないよ!", "There is no {}th saved work!", "{} 번째로 저장된 작품은 아니야!", "¡No hay {}th trabajo guardado!"]
    this_item_found = ["このアイテムが見つかったよ!: {} {}", "This item was found!: {} {}", "이 항목을 발견 했어!: {} {}", "¡Este elemento fue encontrado!: {} {}"]
    list_description = ["左の数字がアイテム番号、その横の名前がアイテム名称だよ!\n", "The number on the left is the item number, and the name next to it is the item name!\n", "왼쪽의 숫자 아이템 번호 옆의 이름이 항목 명칭이야!\n", "El número de la izquierda es el número de artículo y el nombre junto a él es el nombre del artículo.\n"]
    list_base_title = ["色一覧", "base list", "base목록", "lista base"]
    showing_page = ["1 / {} ページを表示中", "current page 1 / {} ", "1 / {} 페이를보기", "1 / {} Página de visualización"]
    list_weapon_title = ["武器一覧", "Weapon list", "무기 목록", "lista de arma"]











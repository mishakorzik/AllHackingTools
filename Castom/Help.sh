
echo "Files and base commands:"

echo "ls – список файлов и каталогов"
echo "ls -al – форматированный список со скрытыми каталогами и файлами"
echo "cd dir – сменить директорию на dir"
echo "cd – сменить на домашний каталог"
echo "pwd – показать текущий каталог"
echo "mkdir dir – создать каталог dir"
echo "rm -rf file – удалить file или папку"
echo "rm -r dir – удалить каталог dir"
echo "rm -r -f /path – удалить каталог dir"
echo "rm -f file – удалить форсированно file"
echo "rm -rf dir – удалить форсированно каталог dir"
echo "cp file1 file2 – скопировать file1 в file2"
echo "cp -r dir1 dir2 – скопировать dir1 в dir2; создаст каталог dir2, если он не существует"
echo "mv file1 file2 – переименовать или переместить file1 в file2. если file2 существующий каталог — переместить file1 в каталог file2"
echo "ln -s file link – создать символическую ссылку link к файлу file"
echo "touch file – создать file"
echo "cat > file – направить стандартный ввод в file"
echo "more file – вывести содержимое file"
echo "head file – вывести первые 10 строк file"
echo "tail file – вывести последние 10 строк file"
echo "tail -f file – вывести содержимое file по мере роста, начинает с последних 10 строк"

echo "Process controlers:"

echo "ps – вывести ваши текущие активные процессы"
echo "top – показать все запущенные процессы"
echo "kill pid – убить процесс с id pid"
echo "killall proc – убить все процессы с именем proc"
echo "bg – список остановленных и фоновых задач; продолжить выполнение остановленной задачи в фоне"
echo "fg – выносит на передний план последние задачи"
echo "fg n – вынести задачу n на передний план"

echo "Access rights and files"

echo "chmod octal file – сменить права file на octal, раздельно для пользователя, группы и для всех добавлением:"
echo "4 – чтение (r)"
echo "2 – запись (w)"
echo "1 – исполнение (x)"

echo "SSH:"

echo "ssh user@host – подключится к host как user"
echo "ssh -p port user@host – подключится к host на порт port как user"
echo "ssh-copy-id user@host – добавить ваш ключ на host для user чтобы включить логин без пароля и по ключам"

echo "Search:"

echo "grep pattern files – искать pattern в files"
echo "grep -r pattern dir – искать рекурсивно pattern в dir"
echo "command | grep pattern – искать pattern в выводе command"
echo "locate file – найти все файлы с именем file"

echo "System Information"

echo "date – вывести текущую дату и время"
echo "cal – вывести календарь на текущий месяц"
echo "uptime – показать текущий аптайм"
echo "whoami – имя, под которым вы залогинены"
echo "uname -a – показать информацию о ядре"
echo "cat /proc/cpuinfo – информация ЦПУ"
echo "cat /proc/meminfo – информация о памяти"
echo "man command – показать мануал для command"
echo "df – показать инф. о использовании дисков"
echo "du – вывести “вес” текущего каталога"
echo "free – использование памяти и swap"
echo "whereis app – возможное расположение программы app"
echo "which app – какая app будет запущена по умолчанию"

echo "Archive:"

echo "tar cf file.tar files – создать tar-архив с именем file.tar содержащий files"
echo "tar xf file.tar – распаковать file.tar"
echo "tar czf file.tar.gz files – создать архив tar с сжатием Gzip"
echo "tar xzf file.tar.gz – распаковать tar с Gzip"
echo "tar cjf file.tar.bz2 – создать архив tar с сжатием Bzip2"
echo "tar xjf file.tar.bz2 – распаковать tar с Bzip2"
echo "gzip file – сжать file и переименовать в file.gz"
echo "gzip -d file.gz – разжать file.gz в file"

echo "Network:"

echo "ping host – пропинговать host и вывести результат"
echo "whois domain – получить информацию whois для domain"
echo "dig domain – получить DNS информацию domain"
echo "dig -x host – реверсивно искать host"
echo "wget file – скачать file"
echo "wget -c file – продолжить остановленную закачку"

echo "Installing packages and working with them"

echo "pkg install package - устанавливает package"
echo "pkg remove package - удаляет package"
echo "pkg search package - ищет в репозитории package"
echo "pkg list-installed - выведет список установленных пакетов"

echo "installation from source codes:"

echo "./configure"
echo "make"
echo "make install"

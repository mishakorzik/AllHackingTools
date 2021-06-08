
echo Files and base commands:

echo ls – список файлов и каталогов
echo ls -al – форматированный список со скрытыми каталогами и файлами
echo cd dir – сменить директорию на dir
echo cd – сменить на домашний каталог
echo pwd – показать текущий каталог
echo mkdir dir – создать каталог dir
echo rm file – удалить file
echo rm -r dir – удалить каталог dir
echo rm -r -f /path – удалить каталог dir
echo rm -f file – удалить форсированно file
echo rm -rf dir – удалить форсированно каталог dir
echo cp file1 file2 – скопировать file1 в file2
echo cp -r dir1 dir2 – скопировать dir1 в dir2; создаст каталог dir2, если он не существует
echo mv file1 file2 – переименовать или переместить file1 в file2. если file2 существующий каталог — переместить file1 в каталог file2
echo ln -s file link – создать символическую ссылку link к файлу file
echo touch file – создать file
echo cat > file – направить стандартный ввод в file
echo more file – вывести содержимое file
echo head file – вывести первые 10 строк file
echo tail file – вывести последние 10 строк file
echo tail -f file – вывести содержимое file по мере роста, начинает с последних 10 строк

Process controlers:

ps – вывести ваши текущие активные процессы
top – показать все запущенные процессы
kill pid – убить процесс с id pid
killall proc – убить все процессы с именем proc
bg – список остановленных и фоновых задач; продолжить выполнение остановленной задачи в фоне
fg – выносит на передний план последние задачи
fg n – вынести задачу n на передний план
Права доступа на файлы
chmod octal file – сменить права file на octal, раздельно для пользователя, группы и для всех добавлением:
4 – чтение (r)
2 – запись (w)
1 – исполнение (x)

SSH:

ssh user@host – подключится к host как user
ssh -p port user@host – подключится к host на порт port как user
ssh-copy-id user@host – добавить ваш ключ на host для user чтобы включить логин без пароля и по ключам

Search:

grep pattern files – искать pattern в files
grep -r pattern dir – искать рекурсивно pattern в dir
command | grep pattern – искать pattern в выводе command
locate file – найти все файлы с именем file
Системная информация

date – вывести текущую дату и время
cal – вывести календарь на текущий месяц
uptime – показать текущий аптайм
whoami – имя, под которым вы залогинены
uname -a – показать информацию о ядре
cat /proc/cpuinfo – информация ЦПУ
cat /proc/meminfo – информация о памяти
man command – показать мануал для command
df – показать инф. о использовании дисков
du – вывести “вес” текущего каталога
free – использование памяти и swap
whereis app – возможное расположение программы app
which app – какая app будет запущена по умолчанию

Archive:

tar cf file.tar files – создать tar-архив с именем file.tar содержащий files
tar xf file.tar – распаковать file.tar
tar czf file.tar.gz files – создать архив tar с сжатием Gzip
tar xzf file.tar.gz – распаковать tar с Gzip
tar cjf file.tar.bz2 – создать архив tar с сжатием Bzip2
tar xjf file.tar.bz2 – распаковать tar с Bzip2
gzip file – сжать file и переименовать в file.gz
gzip -d file.gz – разжать file.gz в file

Network:

ping host – пропинговать host и вывести результат
whois domain – получить информацию whois для domain
dig domain – получить DNS информацию domain
dig -x host – реверсивно искать host
wget file – скачать file
wget -c file – продолжить остановленную закачку
Установка пакетов и работа с ними

pkg install package - устанавливает package
pkg remove package - удаляет package
pkg search package - ищет в репозитории package
pkg list-installed - выведет список установленных пакетов

installation from source codes:

./configure
make
make install

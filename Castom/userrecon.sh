trap 'printf "\n";partial;exit 1' 2

banner() {



printf "                                                   \e[1;92m.-\"\"\"\"-. \e[0m\n"
printf "                                                  \e[1;92m/        \ \e[0m\n"
printf "\e[1;77m  _   _               ____                       \e[0m\e[1;92m/_        _\ \e[0m\n"
printf "\e[1;77m | | | |___  ___ _ __|  _ \ ___  ___ ___  _ __  \e[0m\e[1;92m// \      / \\ \e[0m\n"
printf "\e[1;77m | | | / __|/ _ \ '__| |_) / _ \/ __/ _ \| '_ \ \e[0m\e[1;92m|\__\    /__/| \e[0m\n"
printf "\e[1;77m | |_| \__ \  __/ |  |  _ <  __/ (_| (_) | | | | \e[0m\e[1;92m\    ||    / \e[0m\n"
printf "\e[1;77m  \___/|___/\___|_|  |_| \_\___|\___\___/|_| |_|  \e[0m\e[1;92m\        / \e[0m\n"
printf "                   \e[1;92mv1.0, Author: NONE           \e[0m   \e[1;92m\  __  / \e[0m\n"
printf "                                                    \e[1;92m'.__.' \e[0m\n"
                                                


}

partial() {

if [[ -e $username.txt ]]; then
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Saved:\e[0m\e[1;77m %s.txt\n" $username
fi


}

scanner() {

read -p $'\e[1;92m[\e[0m\e[1;77m?\e[0m\e[1;92m] Input Username:\e[0m ' username

if [[ -e $username.txt ]]; then
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Removing previous file:\e[0m\e[1;77m %s.txt" $username
rm -rf $username.txt
fi
printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Checking username\e[0m\e[1;77m %s\e[0m\e[1;92m on: \e[0m\n" $username

## INSTAGRAM

check_insta=$(curl -s -H "Accept-Language: en" "https://www.instagram.com/$username" -L | grep -o 'The link you followed may be broken'; echo $?)
printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Instagram: \e[0m"

if [[ $check_insta == *'1'* ]]; then
printf "\e[1;92m Found!\e[0m https://www.instagram.com/%s\n" $username
printf "https://www.instagram.com/%s\n" $username > $username.txt
elif [[ $check_insta == *'0'* ]]; then
printf "\e[1;93mNot Found!\e[0m\n"
fi

## Facebook

printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Facebook: \e[0m"
check_face=$(curl -s "https://www.facebook.com/$username" -L -H "Accept-Language: en" | grep -o 'not found'; echo $?)


if [[ $check_face == *'1'* ]]; then
printf "\e[1;92m Found!\e[0m https://www.facebook.com/%s\n" $username
printf "https://www.facebook.com/%s\n" $username >> $username.txt
elif [[ $check_face == *'0'* ]]; then
printf "\e[1;93mNot Found!\e[0m\n"
fi

## TWITTER 

printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Twitter: \e[0m"
check_twitter=$(curl -s "https://www.twitter.com/$username" -L -H "Accept-Language: en" | grep -o 'page doesn’t exist'; echo $?)


if [[ $check_twitter == *'1'* ]]; then
printf "\e[1;92m Found!\e[0m https://www.twitter.com/%s\n" $username
printf "https://www.twitter.com/%s\n" $username >> $username.txt
elif [[ $check_twitter == *'0'* ]]; then
printf "\e[1;93mNot Found!\e[0m\n"
fi

## YOUTUBE

printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] YouTube: \e[0m"
check_youtube=$(curl -s "https://www.youtube.com/$username" -L -H "Accept-Language: en" | grep -o 'Not Found'; echo $?)


if [[ $check_youtube == *'1'* ]]; then
printf "\e[1;92m Found!\e[0m https://www.youtube.com/%s\n" $username
printf "https://www.youtube.com/%s\n" $username >> $username.txt
elif [[ $check_youtube == *'0'* ]]; then
printf "\e[1;93mNot Found!\e[0m\n"
fi

## BLOGGER

printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Blogger: \e[0m"
check=$(curl -s "https://$username.blogspot.com" -L -H "Accept-Language: en" -i | grep -o 'HTTP/2 404'; echo $?)


if [[ $check == *'1'* ]]; then
printf "\e[1;92m Found!\e[0m https://%s.blogspot.com\n" $username
printf "https://%s.blogspot.com\n" $username >> $username.txt
elif [[ $check == *'0'* ]]; then
printf "\e[1;93mNot Found!\e[0m\n"
fi

## GLOOGLE PLUS

printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] GooglePlus: \e[0m"
check=$(curl -s "https://plus.google.com/+$username/posts" -L -H "Accept-Language: en" -i | grep -o 'HTTP/2 404' ; echo $?)


if [[ $check == *'1'* ]]; then
printf "\e[1;92m Found!\e[0m https://plus.google.com/+%s/posts\n" $username
printf "https://plus.google.com/+%s/posts\n" $username >> $username
elif [[ $check == *'0'* ]]; then
printf "\e[1;93mNot Found!\e[0m\n"
fi

## REDDIT

printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Reddit: \e[0m"
check1=$(curl -s -i "https://www.reddit.com/user/$username" -H "Accept-Language: en" -L --user-agent '"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801"' | head -n1 | grep -o 'HTTP/2 404' ; echo $?)

if [[ $check1 == *'0'* ]] ; then 
printf "\e[1;93mNot Found!\e[0m\n"
elif [[ $check1 == *'1'* ]]; then 

printf "\e[1;92m Found!\e[0m https://www.reddit.com/user/%s\n" $username
printf "https://www.reddit.com/user/%s\n" $username >> $username.txt
fi

## WORDPRESS

printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Wordpress: \e[0m"
check1=$(curl -s -i "https://$username.wordpress.com" -H "Accept-Language: en" -L --user-agent '"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801"' | grep -o 'Do you want to register' ; echo $?)

if [[ $check1 == *'0'* ]] ; then 
printf "\e[1;93mNot Found!\e[0m\n"
elif [[ $check1 == *'1'* ]]; then 

printf "\e[1;92m Found!\e[0m https://%s.wordpress.com\n" $username
printf "https://%s.wordpress.com\n" $username >> $username.txt
fi

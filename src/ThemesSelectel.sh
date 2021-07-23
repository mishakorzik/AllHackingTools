echo "------------------------------"
echo "|   Please select a option                            "
echo "|------- ----   --   ----------         --------- ---|"
echo "| 1. Default                                          "
echo "| 2. Neon                                             "
echo "| 3. GoogleDark                                      |"
echo "| 4. Materia                                         |"
echo "| 5. Material                                         "
echo "| 6. Smyck                                            "
echo "| 7. Dracula                                          "
echo "| 8. Twilight                                        |"
echo "|                                                    |"
echo "| While   1/2/3/4/5/6/7/8:                           |"
echo "----------------                                ------"
read numb
if [ $numb = "1" ]
then
        cd
        cd AllHackingTools
        bash Themes/Default.sh
else
        if [ $numb = "2" ]
        then

                cd
                cd AllHackingTools
                bash Themes/Neon.sh
        else
                if [ $numb = "3" ]
                then
                        cd
                        cd AllHackingTools
                        bash Themes/GoogleDark.sh
                else
                        if [ $numb = "4" ]
                        then
                                cd
                                cd AllHackingTools
                                bash Themes/Materia.sh
                        else
                                if [ $numb = "5" ]
                                then
                                        cd
                                        cd AllHackingTools
                                        bash Themes/Material.sh
                                else
                                        if [ $numb = "6" ]
                                        then
                                                cd
                                                cd AllHackingTools
                                                bash Themes/Smyck.sh
                                        else
                                                if [ $numb = "7" ]
                                                then
                                                        cd
                                                        cd AllHackingTools
                                                        bash Themes/Dracula.sh
                                                else
                                                        if [ $numb = "8" ]
                                                        then
                                                                cd
                                                                cd AllHackingTools
                                                                bash Themes/Twilight.sh
                                                        else
                                                                echo "Invalid input! Reloading Tool"
                                                                cd && cd AllHackingTools && bash src/ThemesSelectel.sh
                                                        fi
                                                fi
                                        fi



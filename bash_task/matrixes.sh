#!/bin/bash

# проверка количества аргументов
if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <файл_матрицы1> <файл_матрицы2>"
    exit 1
fi

file1=$1
file2=$2

# проверка существования
if [ ! -f "$file1" ] || [ ! -f "$file2" ]; then
    echo "Ошибка: один или оба файла не найдены."
    exit 1
fi

result=""

# читка файлов
while IFS= read -r line1 && IFS= read -r line2 <&3; do
    # сплиты по пробелу
    row1=($line1)
    row2=($line2)

    # проверка размера
    if [ "${#row1[@]}" -ne "${#row2[@]}" ]; then
        echo "Ошибка: строки матриц разного размера."
        exit 1
    fi

    result_row=()
    for i in "${!row1[@]}"; do
        sum=$((row1[i] + row2[i]))
        result_row+=("$sum")
    done

    result+="${result_row[*]}\n"
done <"$file1" 3<"$file2"

# Выводим итоговую матрицу
echo -e "$result"

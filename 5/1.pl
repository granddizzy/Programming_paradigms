% Рекурсивный вариант
% Базовый случай: если список пустой, то сумма элементов равна 0.
% Это условие завершает рекурсию, когда мы доходим до пустого списка.
sum_list([], 0).

% Рекурсивный случай: если список не пустой, то:
% 1. Разбиваем список на голову (Head) и хвост (Tail).
% 2. Рекурсивно находим сумму элементов хвоста (TailSum).
% 3. Складываем голову списка (Head) с результатом суммы хвоста (TailSum),
%    получая сумму для всего списка.
sum_list([Head | Tail], Sum) :-
    % Рекурсивно вызываем sum_list для хвоста списка (Tail).
    % Эта функция вычисляет сумму элементов Tail.
    sum_list(Tail, TailSum),

    % Вычисляем общую сумму: добавляем голову списка (Head) к результату рекурсии для Tail.
    Sum is Head + TailSum.

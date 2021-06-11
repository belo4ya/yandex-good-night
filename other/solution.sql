-- create table salary
--     (
--      user_id int,
--      d_from date,
--      wage numeric
--     );
-- Есть таблица с логом изменения заплат людей.
-- т.е  user_id=1  c '2021-01-01' до '2021-02-01' получал 10, а сейчас получает 11.
-- никаких увольнений, все работают вечно.
--
-- Надо получить таблицу с текущей wage, то что отдадим бухгалтерам.
-- 1 - 11
-- 2 - 9

-- 1
select user_id, wage from salary s0
where s0.d_from = (
    select max(s1.d_from) from salary s1
    where s1.user_id = s0.user_id
    );

-- 2
select user_id, wage from (
    select user_id, wage, row_number() over(
        partition by user_id order by d_from desc
        ) row from salary
    ) t
where t.row = 1;

-- и завернуть это во view для бухгалтерии
create view if not exists for_accounting (user_id, wage)
as
select user_id, wage from (
    select user_id, wage, row_number() over(
        partition by user_id order by d_from desc
        ) row from salary
    ) t
where t.row = 1;

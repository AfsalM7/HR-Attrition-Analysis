USE hr_attrition;


-- Query 1: Overall Attrition Rate
SELECT 
    Attrition,
    COUNT(*) as employee_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employee_attrition), 2) as percentage
FROM employee_attrition
GROUP BY Attrition;

-- Query 2: Attrition by OverTime (using Window Function)
SELECT 
    OverTime,
    Attrition,
    COUNT(*) as employee_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY OverTime), 2) as pct_within_overtime
FROM employee_attrition
GROUP BY OverTime, Attrition
ORDER BY OverTime, Attrition;

-- Query 3: Attrition by Job Role (using Window Function)
SELECT 
    JobRole,
    Attrition,
    COUNT(*) as employee_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY JobRole), 2) as pct_within_role
FROM employee_attrition
GROUP BY JobRole, Attrition
ORDER BY JobRole, Attrition;
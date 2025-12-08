set_a = {'IDOR', 'CSRF', 'XSS'} #веб
set_b = {'SSRF', 'MITM', 'CSRF'} #мобайл
print('Общие уязвимости: ', set_a & set_b)
print('Только в мобайле: ', set_b-set_a)

from etl.test.full_to_alter import AlternameProcessor

AL = AlternameProcessor()

a = 0
with open('linshi01.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        if len(i) > 2:
            company = i.replace('\n', '')
            result = AL.run_find_simple_name(company)
            with open('linshi02.txt', 'a+', encoding='utf-8') as f1:
                print(result)
                result_linshi = ''
                for each_result in result:
                    result_linshi += each_result + '\t'
                f1.write(i.replace('\n', '')+'\t'+result_linshi+'\n')



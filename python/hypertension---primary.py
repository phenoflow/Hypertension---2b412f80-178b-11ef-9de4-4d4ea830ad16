# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"7Q01.00","system":"readv2"},{"code":"6624","system":"readv2"},{"code":"14A2.00","system":"readv2"},{"code":"6146200","system":"readv2"},{"code":"G203.00","system":"readv2"},{"code":"9OI9.00","system":"readv2"},{"code":"G20z.11","system":"readv2"},{"code":"G202.00","system":"readv2"},{"code":"16292","system":"readv2"},{"code":"72030","system":"readv2"},{"code":"204","system":"readv2"},{"code":"8732","system":"readv2"},{"code":"44549","system":"readv2"},{"code":"63000","system":"readv2"},{"code":"61166","system":"readv2"},{"code":"93055","system":"readv2"},{"code":"50157","system":"readv2"},{"code":"63164","system":"readv2"},{"code":"15106","system":"readv2"},{"code":"43935","system":"readv2"},{"code":"96743","system":"readv2"},{"code":"62718","system":"readv2"},{"code":"52127","system":"readv2"},{"code":"10818","system":"readv2"},{"code":"68659","system":"readv2"},{"code":"52621","system":"readv2"},{"code":"67232","system":"readv2"},{"code":"66567","system":"readv2"},{"code":"6702","system":"readv2"},{"code":"29310","system":"readv2"},{"code":"3979","system":"readv2"},{"code":"11056","system":"readv2"},{"code":"16173","system":"readv2"},{"code":"52427","system":"readv2"},{"code":"13188","system":"readv2"},{"code":"61660","system":"readv2"},{"code":"85944","system":"readv2"},{"code":"22333","system":"readv2"},{"code":"3425","system":"readv2"},{"code":"7057","system":"readv2"},{"code":"18590","system":"readv2"},{"code":"28684","system":"readv2"},{"code":"18057","system":"readv2"},{"code":"19070","system":"readv2"},{"code":"57987","system":"readv2"},{"code":"21837","system":"readv2"},{"code":"16565","system":"readv2"},{"code":"21826","system":"readv2"},{"code":"37086","system":"readv2"},{"code":"43664","system":"readv2"},{"code":"20497","system":"readv2"},{"code":"1894","system":"readv2"},{"code":"44350","system":"readv2"},{"code":"63466","system":"readv2"},{"code":"3712","system":"readv2"},{"code":"39649","system":"readv2"},{"code":"62432","system":"readv2"},{"code":"8857","system":"readv2"},{"code":"31464","system":"readv2"},{"code":"72668","system":"readv2"},{"code":"31816","system":"readv2"},{"code":"18765","system":"readv2"},{"code":"15377","system":"readv2"},{"code":"18482","system":"readv2"},{"code":"95334","system":"readv2"},{"code":"21660","system":"readv2"},{"code":"32423","system":"readv2"},{"code":"69753","system":"readv2"},{"code":"95359","system":"readv2"},{"code":"799","system":"readv2"},{"code":"30770","system":"readv2"},{"code":"4372","system":"readv2"},{"code":"83473","system":"readv2"},{"code":"4668","system":"readv2"},{"code":"8296","system":"readv2"},{"code":"27511","system":"readv2"},{"code":"73586","system":"readv2"},{"code":"60655","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypertension-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypertension---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypertension---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypertension---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

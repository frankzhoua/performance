using System;
using System.IO;
using CalMeass;
using OfficeOpenXml;

namespace CSVReader
{
    //修改excel文件路径 和 统计地址文件路径
    class Program
    {
       // public static string filePath = @"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\performance_nossl_result_1109.xlsx";
        public static string filePath = @"D:\Tests\Benchmark\statistics\performance_result_1113.xlsx";
        //"D:\Tests\Benchmark\statistics\performance_result_1113.xlsx"
        //"D:\benchmark_txt\performance_result_1113.xlsx"
        static void Main(string[] args)
        {
            string[] data;
            writeAddress();
            CalMea calMea = new CalMea();
            //p
            for (int i = 1; i < 6; i++)
            {
                Console.WriteLine("P" + i);
                //data = calMea.calute(@"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Down\P" + i);
                //"D:\benchmark\P3" "D:\Tests\Benchmark\statistics\Down"
                data = calMea.calute(@"D:\Tests\Benchmark\statistics\Down\P" + i);
                writeResult(data, i + 3);
                //Console.WriteLine("P" + i + " - 副本");
                //data = calMea.calute(@"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Down\P" + i + " - 副本");
                //writeResult(data, i + 12);
            }
            //sc
            for (int i = 0; i < 7; i++)
            {
                Console.WriteLine("SC" + i);
                data = calMea.calute(@"D:\Tests\Benchmark\statistics\Down\SC" + i);
                writeResult(data, i + 13);

                //Console.WriteLine("SC" + i);
                //data = calMea.calute(@"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Down\SC" + i);
                //writeResult(data, i + 22);
                //Console.WriteLine("SC" + i + " - 副本");
                //data = calMea.calute(@"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Down\SC" + i + " - 副本");
                //writeResult(data, i + 33);
            }
            //bc
            for (int i = 0; i < 7; i++)
            {
                Console.WriteLine("BC" + i);
                //"D:\benchmark\BC0"
                //data = calMea.calute(@"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Down\BC" + i);
                data = calMea.calute(@"D:\Tests\Benchmark\statistics\Down\BC" + i);
                writeResult(data, i + 24);

                //Console.WriteLine("BC" + i);
                //data = calMea.calute(@"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Down\BC" + i);
                //writeResult(data, i + 44);
                //Console.WriteLine("BC" + i + " - 副本");
                //data = calMea.calute(@"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Down\BC" + i + " - 副本");
                //writeResult(data, i + 55);
            }


        }
        public static void writeResult(string[] data, int row)
        {
            FileInfo fileInfo = new FileInfo(filePath);
            using (ExcelPackage excelPackage = new ExcelPackage(fileInfo))
            {
                ExcelWorkbook excelWorkbook = excelPackage.Workbook;
                ExcelWorksheet excelWorksheet = excelWorkbook.Worksheets[0];
                excelWorksheet.Cells[row, 12].Value = data[0];
                excelWorksheet.Cells[row, 13].Value = data[1];
                excelWorksheet.Cells[row, 14].Value = data[2];
                excelWorksheet.Cells[row, 15].Value = data[3];
                excelWorksheet.Cells[row, 16].Value = data[4];
                excelWorksheet.Cells[row, 17].Value = data[5];
                excelPackage.Save();
            }
        }
        public static void writeAddress()
        {
            string filePath1 = @"D:\Tests\Benchmark\statistics\Statistics.txt";
            string[] lines = File.ReadAllLines(filePath1);
            FileInfo fileInfo = new FileInfo(filePath);
            using (ExcelPackage excelPackage = new ExcelPackage(fileInfo))
            {
                ExcelWorkbook excelWorkbook = excelPackage.Workbook;
                ExcelWorksheet excelWorksheet = excelWorkbook.Worksheets[0];
                int i = 0;
                //只Nossl
                for (int k = 4; k < 31; k++)
                {
                    if (k == 9 || k == 20 )
                        k = k + 4;

                    for (int j = 19; j < 29; j++)
                    {
                        excelWorksheet.Cells[k, j].Value = lines[i++];
                    }
                }

                ////全部
                //for (int k = 4; k < 62; k++)
                //{
                //    if(k == 9 || k == 18 || k== 29 || k == 40 || k == 51 )
                //        k = k + 4;

                //    for (int j = 19; j < 29; j++)
                //    {
                //        excelWorksheet.Cells[k, j].Value = lines[i++];
                //    }
                //}
                excelPackage.Save();
            }

        }
    }
}
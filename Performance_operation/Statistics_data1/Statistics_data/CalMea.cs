using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CalMeass
{
    public class CalMea
    {
        public string[] calute(string folderPath)
        {
            // folderPath = @"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Down\P1"; // 替换为目标文件夹的实际路径
            string[] csvFiles = Directory.GetFiles(folderPath, "*.csv"); // 获取目标文件夹中所有CSV文件

            List<double> prsValues = new List<double>();
            List<double> timeValues = new List<double>();
            List<double> pct50Values = new List<double>();
            List<double> pct90Values = new List<double>();
            List<double> pct99Values = new List<double>();
            List<double> pct9999Values = new List<double>();

            foreach (string csvFile in csvFiles)
            {
                // 读取CSV文件
                string[] lines = File.ReadAllLines(csvFile);
                if (lines.Length >= 2)
                {
                    // 解析第二行数据
                    string[] values = lines[1].Split(',');
                    if (values.Length >= 10)
                    {
                        double prsValue, timeValue, pct50Value, pct90Value, pct99Value, pct9999Value;

                        // 解析第五列数据
                        if (double.TryParse(values[4], out prsValue))
                            prsValues.Add(prsValue);

                        // 解析第六列数据
                        if (double.TryParse(values[5], out timeValue))
                            timeValues.Add(timeValue);

                        // 解析第七列数据
                        if (double.TryParse(values[6], out pct50Value))
                            pct50Values.Add(pct50Value);

                        // 解析第八列数据
                        if (double.TryParse(values[7], out pct90Value))
                            pct90Values.Add(pct90Value);

                        // 解析第九列数据
                        if (double.TryParse(values[8], out pct99Value))
                            pct99Values.Add(pct99Value);

                        // 解析第十列数据
                        if (double.TryParse(values[9], out pct9999Value))
                            pct9999Values.Add(pct9999Value);
                    }
                }
            }

            // 计算中位数
            double medianPRS = CalculateMedian(prsValues);
            double medianTime = CalculateMedian(timeValues);
            double medianPct50 = CalculateMedian(pct50Values);
            double medianPct90 = CalculateMedian(pct90Values);
            double medianPct99 = CalculateMedian(pct99Values);
            double medianPct9999 = CalculateMedian(pct9999Values);

            // 输出结果
            Console.WriteLine($"PRS = {medianPRS}");
            Console.WriteLine($"Time = {medianTime}");
            Console.WriteLine($"50% = {medianPct50}");
            Console.WriteLine($"90% = {medianPct90}");
            Console.WriteLine($"99% = {medianPct99}");
            Console.WriteLine($"99.99% = {medianPct9999}");
            string[] data=new string[] { medianPRS.ToString(), medianTime.ToString(), medianPct50.ToString(), medianPct90.ToString(), medianPct99.ToString(), medianPct9999.ToString() } ;
            return data;


        }
        static double CalculateMedian(List<double> values)
        {
            values.Sort();
            int count = values.Count;
            int middleIndex = count / 2;

            if (count % 2 == 0)
            {
                return (values[middleIndex - 1] + values[middleIndex]) / 2;
            }
            else
            {
                return values[middleIndex];
            }
        }
    }
}

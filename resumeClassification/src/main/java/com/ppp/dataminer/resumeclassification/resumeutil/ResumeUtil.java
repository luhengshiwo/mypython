package com.ppp.dataminer.resumeclassification.resumeutil;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import com.ppp.dataminer.core.config.CoreConfig;
import com.ppp.dataminer.core.file.FileReaderTool;

public class ResumeUtil {
   private static Logger logger = LogManager.getLogger(ResumeUtil.class.getName());

   private static Map<String, Integer> JobTitleMap = new HashMap<String, Integer>();
/**
 * 预先读取出job.csv里面的映射关系
 */
   static {
      String rootpath = "";
      BufferedReader reader = null;
      if (!CoreConfig.IS_LOCAL_MODEL) {
         rootpath = ResumeUtil.class.getClassLoader().getResource("").getPath();
      }
      File inFile = new File(rootpath + "resumeClassModelData/job.csv");
      try {
         reader = new BufferedReader(new InputStreamReader(new FileInputStream(inFile), "UTF-8"));
         String line = reader.readLine();
         while (line != null) {
            String[] items = line.split(",");
            if (items.length == 2) {
               JobTitleMap.put(items[0], Integer.parseInt(items[1]));
            }
            line = reader.readLine();
         }
      } catch (Exception e) {
         logger.error("读取jobcsv错误");
      } finally {
         FileReaderTool.safeClose(reader);
      }
   }
/**
 * 
 * @param positioncome 对简历职位作映射
 * @return 返回简历jobtitle的映射关系
 */
   public static String findPosition(String positioncome) {
      String[] positionall = positioncome.split("、|,|;");
      int nummin = 6;
      for (int i = 0; i < positionall.length; i++) {
         String position = positionall[i];
         if(JobTitleMap.containsKey(position)){
            nummin = JobTitleMap.get(position)<nummin?JobTitleMap.get(position):nummin;
         }
      }// 当这个for循环完成的时候，nummin里面是最小的那个职位，如果没有对应上的话，就是3

      if (nummin == 6) {
         for (int i = 0; i < positionall.length; i++) {
            String position = positionall[i];
            String[] mystr = { "总监", "总经理", "首席", "总裁" };
            for (int j = 0; j < mystr.length; j++) {
               if (position.contains(mystr[j])) {
                  nummin = 5;
               }
            }
         }
      }// 没匹配上的时候用特征词
      if (nummin == 6) {
         nummin = 3;
      }

      return String.valueOf(nummin);

   }

   public static int findSalarylast(int salary_last, int salaryexp) {
      int salary;
      if (salary_last == 0) {
         salary = (int) (salaryexp * 0.8);
      } else {
         salary = salary_last;
      }
      return salary;
   }

}

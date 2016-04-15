package com.ppp.dataminer.resumeclassification.prediction;

/**
 * @author luheng
 */

import java.util.ArrayList;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import weka.clusterers.SimpleKMeans;
import weka.core.Attribute;
import weka.core.DenseInstance;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.SerializationHelper;

import com.ppp.dataminer.core.config.CoreConfig;
import com.ppp.dataminer.resumeclassification.resumestruct.ResumeDetail;

/**
 * 简历分类
 * 
 * @author luheng
 */
public class Resumeprediction {

	private static Logger logger = LogManager.getLogger(Resumeprediction.class
			.getName());
	/**
	 * 读取简历的聚类模型
	 */
	static SimpleKMeans cluster;
	static {
		String rootpath = "";
		if (!CoreConfig.IS_LOCAL_MODEL) {
			rootpath = Resumeprediction.class.getClassLoader().getResource("")
					.getPath();
		}
		try {
			cluster = (SimpleKMeans) SerializationHelper.read(rootpath
					+ "resumeClassModelData/cluster.model");
		} catch (Exception e) {
			cluster = null;
			logger.error("读取聚类模型发生错误");
		}

	}

	/**
	 * 预测模型的主接口
	 * 
	 * @param resume
	 * @return
	 */
	public static int resumeClassification(ResumeDetail resume) {
		int clusterofInst;
		if (cluster == null) {
			logger.info("简历质量分类出错，默认返回3");
			clusterofInst = 3;
		} else {
//			logger.info("简历质量分类开始");

			ArrayList<Object> data = new ArrayList<Object>();

			data.add(resume.getSalaryLast());
			data.add(resume.getWorkMonth());
			data.add(resume.getSalaryExp());
			// try {
			// data.add(resume.getPositionExp());
			// } catch (NumberFormatException e1) {
			// data.add("3");
			// }
			// 暂时不需要jobtitle字段，注掉
			Instances insts = createData(data); // 取出这个数据
			Instance inst = insts.instance(0);// 取出这个数据中的一个实例
			try {
				clusterofInst = cluster.clusterInstance(inst);
			} catch (Exception e) {
				clusterofInst = 2;
				logger.error("预测类别发生错误，默认返回2");
			}
		}

		/*
		 * 如果聚类是0或者1，调整为1，0，使得类标号大小和简历质量一致
		 */
		if (clusterofInst == 0) {
			clusterofInst = 1;
		} else if (clusterofInst == 1) {
			clusterofInst = 0;
		} else if (clusterofInst == 2) {
			clusterofInst = 4;
		}else if (clusterofInst == 3) {
			clusterofInst = 2;
		}else if (clusterofInst == 4) {
			clusterofInst = 3;
		}
		return clusterofInst;
	}

	/**
	 * @createdata 生成一个weka可读的数据
	 */
	private static Instances createData(ArrayList<Object> data) {
		Instances dataSet = formatDataset();

		double[] values = new double[dataSet.numAttributes()];
		values[0] = (Integer) data.get(0);
		values[1] = (Integer) data.get(1);
		values[2] = (Integer) data.get(2);
		// values[3] = dataSet.attribute(3).indexOfValue((String) data.get(3));
		Instance inst = new DenseInstance(1.0, values);
		dataSet.add(inst);
		return dataSet;
	}

	/**
	 * @Instances 生成weka的指定数据格式
	 */
	private static Instances formatDataset() {
		ArrayList<Attribute> atts = new ArrayList<Attribute>();
		Attribute salary_last = new Attribute("salary_last");
		Attribute workmonth = new Attribute("workmonth");
		Attribute salary_exp = new Attribute("salary_exp");
		// ArrayList<String> labels1 = new ArrayList<String>();
		// labels1.add("1");
		// labels1.add("2");
		// labels1.add("3");
		// labels1.add("4");
		// labels1.add("5");
		// Attribute position = new Attribute("position", labels1);
		atts.add(salary_last);
		atts.add(workmonth);
		atts.add(salary_exp);
		// atts.add(position);
		Instances dataSet = new Instances("name", atts, 0);
		return dataSet;
	}

}

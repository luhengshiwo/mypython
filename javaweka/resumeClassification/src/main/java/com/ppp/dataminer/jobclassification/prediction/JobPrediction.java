package com.ppp.dataminer.jobclassification.prediction;

import java.io.IOException;
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
import com.ppp.dataminer.jobclassification.jobstruct.JobDetail;

public class JobPrediction {
	private static Logger logger = LogManager.getLogger(JobPrediction.class
			.getName());

	static SimpleKMeans cluster;
	static {
		String rootpath = "";
		if (!CoreConfig.IS_LOCAL_MODEL) {
			rootpath = JobPrediction.class.getClassLoader().getResource("")
					.getPath();
		}
		try {
			cluster = (SimpleKMeans) SerializationHelper.read(rootpath
					+ "resumeClassModelData/job.model");
		} catch (Exception e) {
			cluster = null;
			logger.error("读取聚类模型发生错误");
		}

	}

	public static int jobClassification(JobDetail job) {
		// 读取训练好的模型
		int clusterofinst;
		if (cluster==null) {
			logger.info("简历质量分类出错，默认返回2");
			clusterofinst = 2;
		} else {
			logger.info("简历质量分类开始");

			ArrayList<Object> data = new ArrayList<Object>();

			data.add(job.getSalary());
			data.add(job.getWorkmonth());
			try {
				data.add(job.getPosition());
			} catch (NumberFormatException e1) {
				data.add("3");
			} catch (IOException e1) {
				data.add("3");
			}
			Instances insts = createData(data); // 取出这个数据
			Instance inst = insts.instance(0);// 取出这个数据中的一个实例
//			System.out.println(inst);
			// System.out.println(cluster.clusterInstance(inst));
			try {
				clusterofinst = cluster.clusterInstance(inst);
			} catch (Exception e) {
				clusterofinst = 2;
				logger.error("预测类别发生错误，默认返回2");
				;
			}
		}

		/*
		 * 调整聚类标号，使得类标号大小和简历质量一致
		 */
		if (clusterofinst == 0) {
			clusterofinst = 3;
		} else if (clusterofinst == 1) {
			clusterofinst = 1;
		} else if (clusterofinst == 2) {
			clusterofinst = 4;
		} else if (clusterofinst == 3) {
			clusterofinst = 2;
		} else if (clusterofinst == 4) {
			clusterofinst = 0;
		}

		return clusterofinst;
	}

	/**
	 * @createdata 生成一个weka可读的数据
	 */
	private static Instances createData(ArrayList<Object> data) {
		Instances dataset = formatDataset();

		double[] values = new double[dataset.numAttributes()];
		values[0] = (Integer) data.get(0);
		values[1] = (Integer) data.get(1);
		values[2] = dataset.attribute(2).indexOfValue((String) data.get(2));
		Instance inst = new DenseInstance(1.0, values);
		dataset.add(inst);
		return dataset;
	}

	/**
	 * @Instances 生成weka的指定数据格式
	 */
	private static Instances formatDataset() {
		ArrayList<Attribute> atts = new ArrayList<Attribute>();
		Attribute salary = new Attribute("salary");
		Attribute workmonth = new Attribute("workmonth");
		ArrayList<String> labels1 = new ArrayList<String>();
		labels1.add("1");
		labels1.add("2");
		labels1.add("3");
		labels1.add("4");
		labels1.add("5");
		Attribute position = new Attribute("position", labels1);
		atts.add(salary);
		atts.add(workmonth);
		atts.add(position);
		Instances dataset = new Instances("name", atts, 0);
		return dataset;
	}

}
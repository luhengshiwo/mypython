package com.ppp.dataminer.jobclassification.training;

import weka.clusterers.SimpleKMeans;
import weka.core.Instances;
import weka.core.SerializationHelper;
import weka.core.converters.ConverterUtils.DataSource;

import com.ppp.dataminer.core.config.CoreConfig;
import com.ppp.dataminer.resumeclassification.training.ResumeTraining;
/**
 * @JobTraining
 *训练出职位聚类模型
 */
public class JobTraining {


	public static void main(String[] args) throws Exception {
		String rootpath="";
		if (!CoreConfig.IS_LOCAL_MODEL) {
			rootpath = ResumeTraining.class.getClassLoader().getResource("").getPath();
		}
		String filename = rootpath + "resumeClassModelData/job.arff";
		Instances data = DataSource.read(filename);
		// System.out.println(data.instance(0));
		String[] options = new String[2];
		options[0] = "-N";
		options[1] = "5";
		SimpleKMeans cluster = new SimpleKMeans();
		cluster.setOptions(options);
		cluster.buildClusterer(data);
//		 System.out.println(cluster);
		SerializationHelper.write(rootpath + "resumeClassModelData/job.model", cluster);

	}
}

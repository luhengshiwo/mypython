package com.ppp.dataminer.resumeclassification.training;
/**
 * @author luheng
 */

import com.ppp.dataminer.core.config.CoreConfig;
import weka.core.Instances;
import weka.core.SerializationHelper;
import weka.clusterers.SimpleKMeans;
import weka.core.converters.ConverterUtils.DataSource;

/**
 * @ResumeTraining
 *训练出聚类模型
 */
public class ResumeTraining {
	public static void main(String[] args) throws Exception {
		String rootpath="";
		if (!CoreConfig.IS_LOCAL_MODEL) {
			rootpath = ResumeTraining.class.getClassLoader().getResource("").getPath();
		}
		String filename = rootpath + "resumeClassModelData/resume.arff";
		Instances data = DataSource.read(filename);
		// System.out.println(data.instance(0));
		String[] options = new String[4];//设定k-means里面的参数
		options[0] = "-N";
		options[1] = "5";
		options[2]="-S";
		options[3] = "15";
		SimpleKMeans cluster = new SimpleKMeans();
		cluster.setOptions(options);
		cluster.buildClusterer(data);
		 System.out.println(cluster);
		SerializationHelper.write(rootpath + "resumeClassModelData/cluster.model", cluster);

	}
}
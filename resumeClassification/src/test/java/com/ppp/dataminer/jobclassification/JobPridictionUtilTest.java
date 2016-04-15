package com.ppp.dataminer.jobclassification;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import com.ppp.dataminer.jobclassification.jobstruct.JobDetail;

import com.ppp.dataminer.jobclassification.prediction.JobPrediction;

;

public class JobPridictionUtilTest extends TestCase {
	/**
	 * Create the test case
	 *
	 * @param testName
	 *            name of the test case
	 */
	public JobPridictionUtilTest(String testName) {
		super(testName);
	}

	/**
	 * @return the suite of tests being tested
	 */
	public static Test suite() {
		return new TestSuite(JobPridictionUtilTest.class);
	}

	/**
	 * Rigourous Test :-)
	 */
	public void testJobPridictionUtil() {
		JobDetail job = new JobDetail();
		job.setSalary(7000);
		job.setWorkmonth(2);
//		System.out.println(JobPrediction.jobClassification(job));
		assertEquals(JobPrediction.jobClassification(job), 1);
	}
	public void testJobPridictionUtil2() {
		JobDetail job = new JobDetail();
		job.setSalary(3000);
		job.setWorkmonth(12);
//		System.out.println(JobPrediction.jobClassification(job));
		assertEquals(JobPrediction.jobClassification(job), 0);
	}
	public void testJobPridictionUtil3() {
		JobDetail job = new JobDetail();
		job.setSalary(5000);
		job.setWorkmonth(20);
//		System.out.println(JobPrediction.jobClassification(job));
		assertEquals(JobPrediction.jobClassification(job), 1);
	}
	public void testJobPridictionUtil4() {
		JobDetail job = new JobDetail();
		job.setSalary(13000);
		job.setWorkmonth(20);
//		System.out.println(JobPrediction.jobClassification(job));
		assertEquals(JobPrediction.jobClassification(job), 4);
	}
	public void testJobPridictionUtil5() {
		JobDetail job = new JobDetail();
		job.setSalary(27000);
		job.setWorkmonth(20);
//		System.out.println(JobPrediction.jobClassification(job));
		assertEquals(JobPrediction.jobClassification(job), 4);
	}
	public void testJobPridictionUtil6() {
		JobDetail job = new JobDetail();
		
		assertEquals(JobPrediction.jobClassification(job), 0);
	}
}

package com.ppp.dataminer.resumestatusanalysis;

import com.ppp.dataminer.resumestatusanalysis.struct.Resumestatusstruct;
import com.ppp.dataminer.resumestatusanalysis.prediction.Resumestatusprediction;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

public class ResumestatuspredictionutilTest extends TestCase {
	/**
	 * Create the test case
	 *
	 * @param testName
	 *            name of the test case
	 */
	public ResumestatuspredictionutilTest(String testName) {
		super(testName);
	}

	/**
	 * @return the suite of tests being tested
	 */
	public static Test suite() {
		return new TestSuite(ResumestatuspredictionutilTest.class);
	}

	/**
	 * Rigourous Test :-)
	 */
	public void testResumestatuspredictionutil() {
		Resumestatusstruct resumestatus = new Resumestatusstruct();
		resumestatus.setLiked(2);
		resumestatus.setDisliked(0);
		resumestatus.setInterview_num(0);
		resumestatus.setDinterview_recommended_num(0);
		resumestatus.setDinterview_interview_num(0);
		resumestatus.setApplied_num(0);
		resumestatus.setLatest_logon_time("0000-00-00 00:00:00");
		resumestatus.setLatest_date_added("0000-00-00 00:00:00");
		double a = Resumestatusprediction.popularity(resumestatus);
		System.out.println(a);
		assertEquals(a, 0.3705001955939895);
		double b = Resumestatusprediction.activeDegree(resumestatus);
		System.out.println(b);
		assertEquals(b,6.694488401456455E-5);//有时候测试会不通过，不同时间结果是不一样的，因为算法依赖于当前时间
	}
	public void testResumestatuspredictionutil2() {
		Resumestatusstruct resumestatus = new Resumestatusstruct();
		resumestatus.setLiked(1);
		resumestatus.setDisliked(0);
		resumestatus.setInterview_num(0);
		resumestatus.setDinterview_recommended_num(0);
		resumestatus.setDinterview_interview_num(0);
		resumestatus.setApplied_num(0);
		resumestatus.setLatest_logon_time("2016-04-01 12:01:20");
		resumestatus.setLatest_date_added("0000-00-00 00:00:00");
		double a = Resumestatusprediction.popularity(resumestatus);
		System.out.println(a);
		assertEquals(a, 0.20658976285529906);
		double b = Resumestatusprediction.activeDegree(resumestatus);
		System.out.println(b);
		assertEquals(b, 0.8806658735961485);//有时候测试会不通过，不同时间结果是不一样的，因为算法依赖于当前时间
	}
	public void testResumestatuspredictionutil3() {
		Resumestatusstruct resumestatus = new Resumestatusstruct();
		resumestatus.setLiked(10);
		resumestatus.setDisliked(0);
		resumestatus.setInterview_num(0);
		resumestatus.setDinterview_recommended_num(0);
		resumestatus.setDinterview_interview_num(0);
		resumestatus.setApplied_num(0);
		resumestatus.setLatest_logon_time("2016-04-01 12:01:20");
		resumestatus.setLatest_date_added("0000-00-0");
		double a = Resumestatusprediction.popularity(resumestatus);
		System.out.println(a);
		System.out.println("3");
		assertEquals(a, 0.9011496986740621);
		double b = Resumestatusprediction.activeDegree(resumestatus);
		System.out.println(b);
		assertEquals(b, 0.8806658735961485);//有时候测试会不通过，不同时间结果是不一样的，因为算法依赖于当前时间
	}
	public void testResumestatuspredictionutil4() {
		Resumestatusstruct resumestatus = new Resumestatusstruct();
		resumestatus.setLiked(10);
//		resumestatus.setDisliked(0); //没有给dislike赋值
		resumestatus.setInterview_num(0);
		resumestatus.setDinterview_recommended_num(0);
		resumestatus.setDinterview_interview_num(0);
		resumestatus.setApplied_num(0);
		resumestatus.setLatest_logon_time("2016-04-01 12:01:20");
		resumestatus.setLatest_date_added("0000-00-0");
		double a = Resumestatusprediction.popularity(resumestatus);
		System.out.println(a);
		assertEquals(a, 0.9011496986740621);
		double b = Resumestatusprediction.activeDegree(resumestatus);
		System.out.println(b);
		assertEquals(b, 0.8806658735961485);//有时候测试会不通过，不同时间结果是不一样的，因为算法依赖于当前时间
	}
}

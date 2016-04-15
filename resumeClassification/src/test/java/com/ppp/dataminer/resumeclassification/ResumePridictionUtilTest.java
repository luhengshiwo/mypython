package com.ppp.dataminer.resumeclassification;

import com.ppp.dataminer.resumeclassification.prediction.Resumeprediction;
import com.ppp.dataminer.resumeclassification.resumestruct.ResumeDetail;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class ResumePridictionUtilTest 
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public ResumePridictionUtilTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( ResumePridictionUtilTest.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testResumePridictionUtil()
    {
    	ResumeDetail resume = new ResumeDetail();
		resume.setSalaryLast(0);
		resume.setWorkMonth(80);
		resume.setSalaryExp(13001);
		int resumeClassification = Resumeprediction.resumeClassification(resume);
//		System.out.println(resumeClassification);
		assertEquals( resumeClassification,4);
    }
    public void testResumePridictionUtil1()
    {
    	ResumeDetail resume = new ResumeDetail();
		resume.setSalaryLast(9000);
		resume.setWorkMonth(10);
		resume.setSalaryExp(13000);
		int resumeClassification = Resumeprediction.resumeClassification(resume);
//		System.out.println(resumeClassification);
		assertEquals( resumeClassification,4);
		
    }
    public void testResumePridictionUtil2()
    {
    	ResumeDetail resume = new ResumeDetail();

		int resumeClassification = Resumeprediction.resumeClassification(resume);
//		System.out.println(resumeClassification);
		assertEquals( resumeClassification,0);
    }
    public void testResumePridictionUtil3()
    {
    	ResumeDetail resume = new ResumeDetail();
		resume.setSalaryLast(19000);
		resume.setWorkMonth(100);
		resume.setSalaryExp(23000);
		int resumeClassification = Resumeprediction.resumeClassification(resume);
//		System.out.println(resumeClassification);
		assertEquals( resumeClassification,4);
		
    }
}
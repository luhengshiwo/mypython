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
		resume.setWorkMonth(42);
		resume.setSalaryExp(14001);
		resume.setPositionExp("商务经理/主管、市场策划/企划专员/助理、区域销售专员/助理、销售经理");
		int resumeClassification = Resumeprediction.resumeClassification(resume);
		assertEquals( resumeClassification,4 );
    }
}
package com.ppp.dataminer.resumeclassification.resumestruct;

/**
 * @author luheng
 */
import com.ppp.dataminer.resumeclassification.resumeconfig.ResumeConfig;
import com.ppp.dataminer.resumeclassification.resumeutil.ResumeUtil;

public class ResumeDetail {
/**
 * salaryLast 上一次的薪资
 *  workMonth  工作经验
 *  salaryExp 期望薪资 
 *  positionExp 期望职位
 */
	private int salaryLast;
	private int workMonth;
	private int salaryExp;
	private String positionExp;

	public ResumeDetail() {
		salaryLast = ResumeConfig.SALARY_LAST_DEFAULT;
		workMonth = ResumeConfig.WORKMONTH;
		salaryExp = ResumeConfig.SALARY_EXP_DEFAULT;
		positionExp = ResumeConfig.POSITION_DEFAULT;
	}

	public int getWorkMonth() {
		return workMonth;
	}

	public void setWorkMonth(int workMonth) {
		this.workMonth = workMonth;
	}

	public int getSalaryExp() {
		return salaryExp;
	}

	public int getSalaryLast() {
		return ResumeUtil.findSalarylast(salaryLast, salaryExp);
	}

	public void setSalaryLast(int salaryLast) {
		this.salaryLast = salaryLast;
	}

	public void setSalaryExp(int salaryExp) {
		this.salaryExp = salaryExp;
	}

	public String getPositionExp() {
		return ResumeUtil.findPosition(positionExp);
	}

	public void setPositionExp(String positionExp) {
		this.positionExp = positionExp;
	}

}

package com.ppp.dataminer.jobclassification.jobstruct;

import java.io.IOException;
import com.ppp.dataminer.jobclassification.jobconfig.JobConfig;
import com.ppp.dataminer.resumeclassification.resumeutil.ResumeUtil;

public class JobDetail {
	/**
	 * salary HR提供的薪资 
	 * workmonth 要求的工作经验 
	 * position 提供的职位名称
	 * position字段暂时不用
	 */
	public int salary;
	public int workmonth;
	public String position;

	public JobDetail() {
		salary = JobConfig.SALARY_DEFULT;
		workmonth = JobConfig.WORKMONTH_DEFULT;
		position = JobConfig.POSITION_DEFAULT;
	}

	public int getSalary() {
		return salary;
	}

	/*
	 * setSalary里面的salary的取法，job薪资salary_start---salary_end的范围，如果salary_start==0，
	 * 取salary_end，否则，取salary_start
	 */
	public void setSalary(int salary) {
		this.salary = salary;
	}

	public int getWorkmonth() {
		return workmonth;
	}

	public void setWorkmonth(int workmonth) {
		this.workmonth = workmonth;
	}

	public String getPosition() throws NumberFormatException, IOException {
		return ResumeUtil.findPosition(position);
	}

	public void setPosition(String position) {
		this.position = position;
	}

}

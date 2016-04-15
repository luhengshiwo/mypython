package com.ppp.dataminer.resumestatusanalysis.prediction;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.ppp.dataminer.resumestatusanalysis.struct.Resumestatusstruct;
import com.ppp.dataminer.resumestatusanalysis.config.Resumestatuspcaconfig;

;

public class Resumestatusprediction {

	private static Logger logger = LogManager
			.getLogger(Resumestatusprediction.class.getName());

	/**
	 * 这个函数返回的是一份简历的受欢迎程度
	 * 
	 * @param resumestatus
	 * @return
	 */
	public static double popularity(Resumestatusstruct resumestatus) {
		int liked = resumestatus.getLiked();
		int disliked = resumestatus.getDisliked();
		int interview_num = resumestatus.getInterview_num();
		int applied_num = resumestatus.getApplied_num();
		int dinterview_interview_num = resumestatus
				.getDinterview_interview_num();
		int dinterview_recommended_num = resumestatus
				.getDinterview_recommended_num();

		double popularitynum = (Resumestatuspcaconfig.LIKED * liked
				+ Resumestatuspcaconfig.DISLIKED * disliked
				+ Resumestatuspcaconfig.APPLIED_NUM * applied_num
				+ Resumestatuspcaconfig.INTERVIEW_NUM * interview_num
				+ Resumestatuspcaconfig.DINTERVIEW_INTERVIEW_NUM
				* dinterview_interview_num + Resumestatuspcaconfig.DINTERVIEW_RECOMMEND_NUM
				* dinterview_recommended_num)
				/ (Resumestatuspcaconfig.LIKED + Resumestatuspcaconfig.DISLIKED
						+ Resumestatuspcaconfig.APPLIED_NUM
						+ Resumestatuspcaconfig.INTERVIEW_NUM
						+ Resumestatuspcaconfig.DINTERVIEW_INTERVIEW_NUM + Resumestatuspcaconfig.DINTERVIEW_RECOMMEND_NUM);
		double popularityScore = 1 - 1 / Math.exp(popularitynum);
		return popularityScore;
	}

	/**
	 * 这个函数返回的是一份简历的活跃度
	 * 
	 * @param resumestatus
	 * @return
	 */
	public static double activeDegree(Resumestatusstruct resumestatus) {
		// 6: "latest_date_added", 7: "lasted_logon_time"
		String latest_date_added = resumestatus.getLatest_date_added();
		String lasted_logon_time = resumestatus.getLatest_logon_time();
		int daymin = Math.min(getdays(latest_date_added),
				getdays(lasted_logon_time));
		double T = 60;
		double activescore = Math.pow(0.5, daymin / T);
		return activescore;

	}

	/**
	 * 这边返回的是输入日期到给定日期之间的时间间隔，单位是天
	 * 
	 * @param date
	 * @return
	 */
	public static int getdays(String date) {
		if (date == "0000-00-00 00:00:00") {
			date = "2014-01-01 00:00:00";
		}
		Date currentTime = new Date();
		SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		int days;
		try {
			// Date currentTime = formatter.parse("2015-11-01 00:00:00");
			Date oldday = formatter.parse(date);
			long diff = currentTime.getTime() - oldday.getTime();
			days = (int) (diff / (1000 * 60 * 60 * 24));
		} catch (ParseException e) {
			logger.error("格式化日期数据发生错误，返回365");
			days = 365;
		}
		return days;
	}

}

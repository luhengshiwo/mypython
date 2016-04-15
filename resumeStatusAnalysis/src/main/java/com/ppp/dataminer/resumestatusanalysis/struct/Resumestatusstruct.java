package com.ppp.dataminer.resumestatusanalysis.struct;

import com.ppp.dataminer.resumestatusanalysis.config.Resumestatusconfig;

public class Resumestatusstruct {

	private int liked;
	private int disliked;
	private int applied_num;
	private int interview_num;
	private int dinterview_interview_num;
	private int dinterview_recommended_num;
	private String latest_date_added;
	private String latest_logon_time;
//	latest_date_added 的格式形如 "2014-01-01 00:00:00" ，若没有值，则形如"0000-00-00 00:00:00"
	
	public Resumestatusstruct(){
		liked=Resumestatusconfig.LIKED_DEFAULT;
		disliked=Resumestatusconfig.DISLIKED_DEFAULT;
		applied_num = Resumestatusconfig.APPLIED_NUM_DEFAULT;
		interview_num = Resumestatusconfig.INTERVIEW_NUM_DEFAULT;
		dinterview_interview_num = Resumestatusconfig.DINTERVIEW_INTERVIEW_NUM_DEFAULT;
		dinterview_recommended_num = Resumestatusconfig.DINTERVIEW_RECOMMEND_NUM_DEFAULT;
		latest_date_added = Resumestatusconfig.LATEST_DATE_ADDED_DEFAULT;
		latest_logon_time = Resumestatusconfig.LATEST_LOGON_TIME_DEFAULT;				
	}
	
	
	public int getLiked() {
		return liked;
	}
	public void setLiked(int liked) {
		this.liked = liked;
	}
	public int getDisliked() {
		return disliked;
	}
	public void setDisliked(int disliked) {
		this.disliked = disliked;
	}
	public int getApplied_num() {
		return applied_num;
	}
	public void setApplied_num(int applied_num) {
		this.applied_num = applied_num;
	}
	public int getInterview_num() {
		return interview_num;
	}
	public void setInterview_num(int interview_num) {
		this.interview_num = interview_num;
	}
	public int getDinterview_interview_num() {
		return dinterview_interview_num;
	}
	public void setDinterview_interview_num(int dinterview_interview_num) {
		this.dinterview_interview_num = dinterview_interview_num;
	}
	public int getDinterview_recommended_num() {
		return dinterview_recommended_num;
	}
	public void setDinterview_recommended_num(int dinterview_recommended_num) {
		this.dinterview_recommended_num = dinterview_recommended_num;
	}
	public String getLatest_date_added() {
		return latest_date_added;
	}
	public void setLatest_date_added(String latest_date_added) {
		this.latest_date_added = latest_date_added;
	}
	public String getLatest_logon_time() {
		return latest_logon_time;
	}
	public void setLatest_logon_time(String latest_logon_time) {
		this.latest_logon_time = latest_logon_time;
	}

}

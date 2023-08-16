# Direct Digital Synthesis (DDS)

Certainly! Imagine you're a painter, but instead of a brush and paint, you're equipped with numbers and math. Your canvas? The world of digital signals. In this vibrant world, Direct Digital Synthesis (DDS) is your superpower. With DDS, you can conjure up any waveform you desire—sine waves, square waves, and everything in between—just by crunching some numbers. 

Picture it as a magical music box: you turn the crank (input a frequency), and out comes a beautiful, pristine wave, ready to serenade the digital world. And the best part? You're the maestro, conducting your waves with pinpoint accuracy, adjusting the tempo (frequency) and volume (amplitude) at your will, all in real-time.

Welcome to the rock-and-roll world of Direct Digital Synthesis!

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(3).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(4).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(5).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(6).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(7).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(8).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(9).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(10).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(11).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(12).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(13).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(14).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(15).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(16).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(17).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(19).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(20).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(21).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(22).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(23).png?raw=true)

Update the ```tb.v``` file with the code below

```verilog
module tb;

wire [15:0]DDS_OUT_tdata; //DDS data (waveform) out is a 16-bit stream
wire DDS_OUT_tvalid;  //Handshaking for indicating that data out is valid
reg aclk;
reg aclken;
reg aresetn;

//Instantiation of Unit Under Test (UUT)
dds_system_wrapper UUT // Instantiation of wrapper for your DDS system
       (.DDS_OUT_tdata(DDS_OUT_tdata),
        .DDS_OUT_tvalid(DDS_OUT_tvalid),
        .aclk(aclk),
        .aclken(aclken),
        .aresetn(aresetn));



parameter half_clk_cycle = 5; // 5ns is one half a clock cycle of a 100 MHz matches

initial begin
    aclken <= 1'b1; // "<=" sets reg simultaneously 
    aresetn <= 1'b1; //Active Low
end
always begin
    aclk = 1'b1; // "=" sets reg sequentially
    #half_clk_cycle; // Wait half a clock cycle
    
    aclk =1'b0;
    #half_clk_cycle;
end
endmodule
```


![Screenshot](../figs/dds_m1_lab1/Screenshot%20(24).png?raw=true)

Click **Run Simulation** along the left side

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(25).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(26).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(27).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(28).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(29).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(30).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(31).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(32).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(33).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(34).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(35).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(36).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(37).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(38).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(39).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(40).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(41).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(42).png?raw=true)

Update ```tb.v``` with the following code:

```verilog
module tb;

wire [15:0]DDS_OUT_tdata; //DDS data (waveform) out is a 16-bit stream
wire DDS_OUT_tvalid;  //Handshaking for indicating that data out is valid
reg aclk;
reg aclken;
reg aresetn;

//***************************************************UPDATE************
reg [15:0]PHZ_INC_tdata;
reg PHZ_INC_tvalid;
//*********************************************************************


//Instantiation of Unit Under Test (UUT)
dds_system_wrapper UUT
       (.DDS_OUT_tdata(DDS_OUT_tdata),
        .DDS_OUT_tvalid(DDS_OUT_tvalid),
        
        //***************************************************UPDATE************
        .PHZ_INC_tdata(PHZ_INC_tdata),
        .PHZ_INC_tvalid(PHZ_INC_tvalid),
        //*********************************************************************
        
        .aclk(aclk),
        .aclken(aclken),
        .aresetn(aresetn));



parameter half_clk_cycle = 5; // 5ns is one half a clock cycle of a 100 MHz matches

initial begin
    aclken <= 1'b1; // "<=" sets reg simultaneously 
    aresetn <= 1'b1; //Active Low
    
    //***************************************************UPDATE************
    PHZ_INC_tdata <= 16'b0001_0000_0000_0000;
    PHZ_INC_tvalid <= 1'b1;
    //*********************************************************************
    
end
always begin
    aclk = 1'b1; // "=" sets reg sequentially
    #half_clk_cycle; // Wait half a clock cycle
    
    aclk =1'b0;
    #half_clk_cycle;
end
endmodule
```

Click **Run Simulation** and observe that you get 6.25 MHz sine wave.  Adjust zoom and settings as usual.


![Screenshot](../figs/dds_m1_lab1/Screenshot%20(43).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(44).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(45).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(46).png?raw=true)

Click **Save**, observe that ```top_level.v``` is now encompassing of all project elements in the hierarchy.

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(52).png?raw=true)

Copy paste from ```dds_system_wrapper.v``` and paste it into ```top_level.v```.  The code is included after the figures to avoid issues.

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(47).png?raw=true)

![Screenshot](../figs/dds_m1_lab1/Screenshot%20(48).png?raw=true)

```verilog
module top_level
(DDS_OUT_tdata,
    DDS_OUT_tvalid,
    PHZ_INC_tdata,
    PHZ_INC_tvalid,
    aclk,
    aclken,
    aresetn);
  output [15:0]DDS_OUT_tdata;
  output DDS_OUT_tvalid;
  input [15:0]PHZ_INC_tdata;
  input PHZ_INC_tvalid;
  input aclk;
  input aclken;
  input aresetn;

  wire [15:0]DDS_OUT_tdata;
  wire DDS_OUT_tvalid;
  wire [15:0]PHZ_INC_tdata;
  wire PHZ_INC_tvalid;
  wire aclk;
  wire aclken;
  wire aresetn;

  assign PHZ_INC_tdata = 16'b0000_1000_0000_0000;
  assign PHZ_INC_tvalid = 1'b1;
  
  dds_system_wrapper dds_system_i
       (.DDS_OUT_tdata(DDS_OUT_tdata),
        .DDS_OUT_tvalid(DDS_OUT_tvalid),
        .PHZ_INC_tdata(PHZ_INC_tdata),
        .PHZ_INC_tvalid(PHZ_INC_tvalid),
        .aclk(aclk),
        .aclken(aclken),
        .aresetn(aresetn));
endmodule
```


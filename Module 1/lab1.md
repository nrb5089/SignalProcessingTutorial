# Direct Digital Synthesis (DDS)

Certainly! Imagine you're a painter, but instead of a brush and paint, you're equipped with numbers and math. Your canvas? The world of digital signals. In this vibrant world, Direct Digital Synthesis (DDS) is your superpower. With DDS, you can conjure up any waveform you desire—sine waves, square waves, and everything in between—just by crunching some numbers. 

Picture it as a magical music box: you turn the crank (input a frequency), and out comes a beautiful, pristine wave, ready to serenade the digital world. And the best part? You're the maestro, conducting your waves with pinpoint accuracy, adjusting the tempo (frequency) and volume (amplitude) at your will, all in real-time.

Welcome to the rock-and-roll world of Direct Digital Synthesis!

![Screenshot (1)]("../figs/dds_m1_lab1/Screenshot%20(1).png"?raw=true)


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
    PHZ_INC_tdata <= 16'b0000_1000_0000_0000;
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
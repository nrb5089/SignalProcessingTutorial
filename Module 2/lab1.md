# What in the world is AXI?

You might still be feeling like you have a major knowledge gap with respect to what AXI exactly "is"...

Advanced eXtensible Interface (AXI), is part of the ARM Advanced Microcontroller Bus Architecture (AMBA), a protocol that defines how different blocks of an integrated circuit communicate with each other. AXI is particularly used for high-speed data transfer between processors and peripherals or between different subsystems. AXI, which is now in its fourth version (AXI4), is used in many System-on-Chip (SoC) designs, and it is particularly popular in designs based on ARM cores.

AXI has a few key features that make it stand out:

- **Separate Channels**: AXI separates communication into five different channels: Read Address, Write Address, Write Data, Read Data, and Write Response. Each channel has its own valid and ready signals, which are used to control the flow of data. This allows it to support high frequencies and low latencies, as each channel can operate independently of the others.

- **Burst Transactions**: AXI supports burst transactions, allowing it to send multiple data items per address phase. This feature improves efficiency for sequential data access.

- **Pipelining**: The AXI protocol is designed to support pipelining, where multiple transactions can be in flight at the same time. This means that while one transaction is being processed, the next transaction can already be started. This feature increases throughput and reduces latency.

- **Out-of-Order Transaction Completion**: Transactions are not required to complete in the same order they were issued. This feature allows for more efficient scheduling of memory accesses.

AXI protocol is commonly used to interface with complex peripherals such as DDR memory controllers, Ethernet controllers, or complex interconnects in a multi-master environment.  In summary, AXI is a powerful, highly flexible bus protocol designed to enable high-speed data transfer between various parts of a complex integrated circuit. Its features support high-frequency operation, burst data transfer, and pipelining, making it suitable for a wide range of applications, especially in high-performance systems.

The following helped reinforce my understanding of things AXI related.


## AXI Basics 1 - Introduction to AXI:
https://support.xilinx.com/s/article/1053914?language=en_US

## AXI Basics 2 - Simulating AXI interfaces with the AXI Verification IP (AXI VIP)

https://support.xilinx.com/s/article/1053935?language=en_US

## AXI Basics 3 - Master AXI4-Lite simulation with the AXI VIP

https://support.xilinx.com/s/article/1058302?language=en_US

## AXI Basics 4 - Using the AXI VIP as protocol checker for an AXI4 Master interface

https://support.xilinx.com/s/article/1062002?language=en_US

## AXI Basics 5 - Create an AXI4-Lite Sniffer IP to use in Xilinx Vivado IP Integrator

https://support.xilinx.com/s/article/1064306?language=en_US

## AXI Basics 6 - Introduction to AXI4-Lite in Vitis HLS

https://support.xilinx.com/s/article/1137153?language=en_US

## AXI Basics 7 - Connecting to the PS using AXI4-Lite and Vitis HLS

https://support.xilinx.com/s/article/1137753?language=en_US

# AXI-Lite Example from scratch 

Creating a complete AXI interface in Verilog is a complex task because of the many features and flexibility of the AXI protocol. A simple example might not fully illustrate the power of AXI.  Here is an example of a simple AXI4-Lite slave. This is a simplified version of the AXI protocol used for peripherals that do not need the full capabilities of AXI. This example has a single 32-bit read/write register.  Please note that AXI4-Lite protocol doesn't support burst transfers and each transaction consists of a single transfer.

```verilog
module axi_lite_slave #(
    parameter ADDR_WIDTH = 4,
    parameter DATA_WIDTH = 32
) (
    input wire clk,
    input wire rst_n,

    // Write address channel
    input wire [ADDR_WIDTH-1:0] awaddr,
    input wire                  awvalid,
    output reg                  awready,

    // Write data channel
    input wire [DATA_WIDTH-1:0] wdata,
    input wire [DATA_WIDTH/8-1:0] wstrb,
    input wire                  wvalid,
    output reg                  wready,

    // Write response channel
    output reg                  bresp,
    output reg                  bvalid,
    input wire                  bready,

    // Read address channel
    input wire [ADDR_WIDTH-1:0] araddr,
    input wire                  arvalid,
    output reg                  arready,

    // Read data channel
    output reg [DATA_WIDTH-1:0] rdata,
    output reg                  rresp,
    output reg                  rvalid,
    input wire                  rready
);

    reg [DATA_WIDTH-1:0] regfile;
    
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            awready <= 1'b0;
            wready <= 1'b0;
            bresp <= 2'b0;
            bvalid <= 1'b0;
            arready <= 1'b0;
            rresp <= 2'b0;
            rvalid <= 1'b0;
        end else begin
            // Write Address Channel
            awready <= !wvalid;

            // Write Data Channel
            if (awready && awvalid && wvalid) begin
                if (wstrb) // Write strobe checks which byte lanes to update
                    regfile <= wdata;
                wready <= 1'b0;
                bvalid <= 1'b1;
            end else if (!bready && bvalid) begin
                wready <= 1'b0;
                bvalid <= 1'b1;
            end else begin
                wready <= 1'b1;
                bvalid <= 1'b0;
            end

            // Write Response Channel
            if (bvalid && bready) 
                bvalid <= 1'b0;
            
            // Read Address Channel
            arready <= !rvalid;
            
            // Read Data Channel
            if (arready && arvalid) begin
                rdata <= regfile;
                rvalid <= 1'b0;
            end else if (!rready && rvalid) begin
                rvalid <= 1'b1;
            end else begin
                rvalid <= 1'b0;
            end
        end
    end

endmodule
```

This example doesn't include all features of AXI (like different types of responses). Please, remember to validate this code within your complete design and application as different use cases might need adjustments.  Typically, you would use a vendor-provided or third-party IP core to handle AXI communication, or you could use a hardware design tool that can generate AXI interfaces for you. Writing an AXI interface from scratch in Verilog is a task that requires careful understanding of the AXI protocol specification.
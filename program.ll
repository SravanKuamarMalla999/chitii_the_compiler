; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %".2" = bitcast [71 x i8]* @"str5" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %"x" = alloca i32
  store i32 10, i32* %"x"
  %"y" = alloca i32
  store i32 20, i32* %"y"
  %".6" = bitcast [12 x i8]* @"str6" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6")
  %"x_load" = load i32, i32* %"x"
  %".8" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %"x_load")
  %".10" = bitcast [12 x i8]* @"str7" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10")
  %"y_load" = load i32, i32* %"y"
  %".12" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %"y_load")
  %"x_load.1" = load i32, i32* %"x"
  %"y_load.1" = load i32, i32* %"y"
  %"multmp" = mul i32 %"y_load.1", 2
  %"addtmp" = add i32 %"x_load.1", %"multmp"
  %"z" = alloca i32
  store i32 %"addtmp", i32* %"z"
  %"z_load" = load i32, i32* %"z"
  %".15" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %"z_load")
  %".17" = bitcast [16 x i8]* @"str8" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17")
  %".19" = alloca i32
  %".20" = bitcast [3 x i8]* @"fmtstrscan" to i8*
  %".21" = call i32 (i8*, ...) @"scanf"(i8* %".20", i32* %".19")
  %".22" = load i32, i32* %".19"
  %"a" = alloca i32
  store i32 %".22", i32* %"a"
  %".24" = bitcast [13 x i8]* @"str9" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24")
  %"a_load" = load i32, i32* %"a"
  %".26" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".26", i32 %"a_load")
  %"x_load.2" = load i32, i32* %"x"
  %"y_load.2" = load i32, i32* %"y"
  %"calltmp" = call i32 @"add"(i32 %"x_load.2", i32 %"y_load.2")
  %"result" = alloca i32
  store i32 %"calltmp", i32* %"result"
  %".29" = bitcast [21 x i8]* @"str11" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29")
  %"result_load" = load i32, i32* %"result"
  %".31" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", i32 %"result_load")
  %".33" = alloca [4 x i32]
  %".34" = getelementptr [4 x i32], [4 x i32]* %".33", i32 0, i32 0
  store i32 5, i32* %".34"
  %".36" = getelementptr [4 x i32], [4 x i32]* %".33", i32 0, i32 1
  store i32 10, i32* %".36"
  %".38" = getelementptr [4 x i32], [4 x i32]* %".33", i32 0, i32 2
  store i32 15, i32* %".38"
  %".40" = getelementptr [4 x i32], [4 x i32]* %".33", i32 0, i32 3
  store i32 20, i32* %".40"
  %".42" = bitcast [24 x i8]* @"str12" to i8*
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".42")
  %"arr_load" = load [4 x i32], [4 x i32]* %".33"
  %".44" = alloca [4 x i32]
  store [4 x i32] %"arr_load", [4 x i32]* %".44"
  %".46" = getelementptr [4 x i32], [4 x i32]* %".44", i32 0, i32 0
  %".47" = load i32, i32* %".46"
  %".48" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i32 %".47")
  %"arr_load.1" = load [4 x i32], [4 x i32]* %".33"
  %".50" = alloca [4 x i32]
  store [4 x i32] %"arr_load.1", [4 x i32]* %".50"
  %".52" = getelementptr [4 x i32], [4 x i32]* %".50", i32 0, i32 1
  %".53" = load i32, i32* %".52"
  %".54" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".55" = call i32 (i8*, ...) @"printf"(i8* %".54", i32 %".53")
  %"arr_load.2" = load [4 x i32], [4 x i32]* %".33"
  %".56" = alloca [4 x i32]
  store [4 x i32] %"arr_load.2", [4 x i32]* %".56"
  %".58" = getelementptr [4 x i32], [4 x i32]* %".56", i32 0, i32 2
  %".59" = load i32, i32* %".58"
  %".60" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".61" = call i32 (i8*, ...) @"printf"(i8* %".60", i32 %".59")
  %"arr_load.3" = load [4 x i32], [4 x i32]* %".33"
  %".62" = alloca [4 x i32]
  store [4 x i32] %"arr_load.3", [4 x i32]* %".62"
  %".64" = getelementptr [4 x i32], [4 x i32]* %".62", i32 0, i32 3
  %".65" = load i32, i32* %".64"
  %".66" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".67" = call i32 (i8*, ...) @"printf"(i8* %".66", i32 %".65")
  %".68" = bitcast [26 x i8]* @"str13" to i8*
  %".69" = call i32 (i8*, ...) @"printf"(i8* %".68")
  %"arr_load.4" = load [4 x i32], [4 x i32]* %".33"
  %".70" = alloca [4 x i32]
  store [4 x i32] %"arr_load.4", [4 x i32]* %".70"
  %".72" = getelementptr [4 x i32], [4 x i32]* %".70", i32 0, i32 2
  %".73" = load i32, i32* %".72"
  %".74" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".75" = call i32 (i8*, ...) @"printf"(i8* %".74", i32 %".73")
  %".76" = getelementptr [4 x i32], [4 x i32]* %".33", i32 0, i32 2
  store i32 100, i32* %".76"
  %".78" = bitcast [39 x i8]* @"str14" to i8*
  %".79" = call i32 (i8*, ...) @"printf"(i8* %".78")
  %"arr_load.5" = load [4 x i32], [4 x i32]* %".33"
  %".80" = alloca [4 x i32]
  store [4 x i32] %"arr_load.5", [4 x i32]* %".80"
  %".82" = getelementptr [4 x i32], [4 x i32]* %".80", i32 0, i32 2
  %".83" = load i32, i32* %".82"
  %".84" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".85" = call i32 (i8*, ...) @"printf"(i8* %".84", i32 %".83")
  %"total" = alloca i32
  store i32 0, i32* %"total"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"arr_load.6" = load [4 x i32], [4 x i32]* %".33"
  %".88" = alloca [4 x i32]
  store [4 x i32] %"arr_load.6", [4 x i32]* %".88"
  %".90" = getelementptr [4 x i32], [4 x i32]* %".88", i32 0, i32 0
  %".91" = load i32, i32* %".90"
  %"arr_load.7" = load [4 x i32], [4 x i32]* %".33"
  %".92" = alloca [4 x i32]
  store [4 x i32] %"arr_load.7", [4 x i32]* %".92"
  %".94" = getelementptr [4 x i32], [4 x i32]* %".92", i32 0, i32 1
  %".95" = load i32, i32* %".94"
  %"addtmp.1" = add i32 %".91", %".95"
  %"arr_load.8" = load [4 x i32], [4 x i32]* %".33"
  %".96" = alloca [4 x i32]
  store [4 x i32] %"arr_load.8", [4 x i32]* %".96"
  %".98" = getelementptr [4 x i32], [4 x i32]* %".96", i32 0, i32 2
  %".99" = load i32, i32* %".98"
  %"addtmp.2" = add i32 %"addtmp.1", %".99"
  %"arr_load.9" = load [4 x i32], [4 x i32]* %".33"
  %".100" = alloca [4 x i32]
  store [4 x i32] %"arr_load.9", [4 x i32]* %".100"
  %".102" = getelementptr [4 x i32], [4 x i32]* %".100", i32 0, i32 3
  %".103" = load i32, i32* %".102"
  %"addtmp.3" = add i32 %"addtmp.2", %".103"
  %"total.1" = alloca i32
  store i32 %"addtmp.3", i32* %"total.1"
  %".105" = bitcast [23 x i8]* @"str15" to i8*
  %".106" = call i32 (i8*, ...) @"printf"(i8* %".105")
  %"total_load" = load i32, i32* %"total.1"
  %".107" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".108" = call i32 (i8*, ...) @"printf"(i8* %".107", i32 %"total_load")
  %".109" = bitcast [22 x i8]* @"str16" to i8*
  %".110" = call i32 (i8*, ...) @"printf"(i8* %".109")
  ret i32 0
}

@"fmtstrint" = internal constant [4 x i8] c"%d\0a\00"
@"fmtstrscan" = internal constant [3 x i8] c"%d\00"
@"str5" = internal constant [71 x i8] c"<<<<<<<<<<<<<<chitti the compiler >>>>>>>>>>>>>>>>> Comprehensive Test\00"
@"str6" = internal constant [12 x i8] c"Value of x:\00"
@"str7" = internal constant [12 x i8] c"Value of y:\00"
@"str8" = internal constant [16 x i8] c"Enter a number:\00"
@"str9" = internal constant [13 x i8] c"You entered:\00"
define i32 @"add"(i32 %"a", i32 %"b")
{
entry:
  %"a.1" = alloca i32
  store i32 %"a", i32* %"a.1"
  %"b.1" = alloca i32
  store i32 %"b", i32* %"b.1"
  %"a_load" = load i32, i32* %"a.1"
  %"b_load" = load i32, i32* %"b.1"
  %"addtmp" = add i32 %"a_load", %"b_load"
  %".6" = bitcast [4 x i8]* @"fmtstrint" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %"addtmp")
  ret i32 %"addtmp"
}

@"str11" = internal constant [21 x i8] c"Result of add(x, y):\00"
@"str12" = internal constant [24 x i8] c"Initial array elements:\00"
@"str13" = internal constant [26 x i8] c"Array element at index 2:\00"
@"str14" = internal constant [39 x i8] c"Array element at index 2 after update:\00"
@"str15" = internal constant [23 x i8] c"Sum of array elements:\00"
@"str16" = internal constant [22 x i8] c"Test program complete\00"
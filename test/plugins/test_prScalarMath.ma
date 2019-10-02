//Maya ASCII 2018 scene
//Name: test_prScalarMath.ma
//Last modified: Mon, Jul 15, 2019 12:53:29 AM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "ACBC7512-43CF-63C7-37F5-0E9B7673477B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 11.829151592674135 6.9600776199534096 11.398928754335193 ;
	setAttr ".r" -type "double3" -29.138352729612603 38.600000000004179 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "1789FA75-42C6-41C7-5B04-A397F3DE65A6";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 21.799100713599884;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "B3EDDDC4-441E-5773-F61D-AD9876CB9C98";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "480506EE-48B6-E9F0-EF49-5B8067FA1527";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "9CFC7B6E-4127-EA82-1BF1-7CABAF2949EE";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "C6D398F6-479E-50B9-7D3E-D18DB9C844C3";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "E5FE914F-4AF2-2AE6-1A10-5796047FD244";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "FB82F24A-4A2D-0B7B-DFC9-86952C7048C3";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "locator";
	rename -uid "495BB61A-409A-0196-FDFD-06A1F807D44B";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 0.5 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "locatorShape" -p "locator";
	rename -uid "7EB7DA73-472C-D322-C48A-2199CB084F0D";
	setAttr -k off ".v";
	setAttr -cb off ".lpx";
	setAttr -cb off ".lpy";
	setAttr -cb off ".lpz";
	setAttr -cb off ".lsx";
	setAttr -cb off ".lsy";
	setAttr -cb off ".lsz";
createNode transform -n "cubes";
	rename -uid "500FA420-43DD-B77F-899A-9BB47132F43D";
	setAttr -l on ".v";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode transform -n "noOperation" -p "cubes";
	rename -uid "2B34EA4C-4F86-91A2-FBEF-7B9B6906012E";
createNode transform -n "noOperation_maya" -p "noOperation";
	rename -uid "6190A7CE-4087-17B9-FC07-7C93A00E04FB";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -5 0.5 -1 ;
createNode mesh -n "noOperation_mayaShape" -p "noOperation_maya";
	rename -uid "DBDF30ED-4BF9-E69F-DF53-05873209C1CD";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "noOperation_pr" -p "noOperation";
	rename -uid "4FF59F81-4AF3-60F0-DB5E-56A33DE61C84";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -5 0 0 ;
createNode mesh -n "noOperation_prShape" -p "noOperation_pr";
	rename -uid "571FEE07-454D-ED3C-1222-82B378E0A56B";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "noOperation_pr_static" -p "noOperation";
	rename -uid "BB6EE3DF-4011-FF56-E3F6-2DBDA0FBF15A";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -5 0 1 ;
createNode mesh -n "noOperation_pr_staticShape" -p "noOperation_pr_static";
	rename -uid "ABF497CC-4127-22EC-6315-C3BA377151A0";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "plusMinusAverage_group" -p "cubes";
	rename -uid "416A9B63-4AA9-9327-5986-6C931DD14A40";
createNode transform -n "sum_maya" -p "plusMinusAverage_group";
	rename -uid "568EA178-486F-3B80-CA94-06AFA8526F28";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -3 1 -1 ;
createNode mesh -n "sum_mayaShape" -p "sum_maya";
	rename -uid "31600D5B-4D2A-76C9-561C-FE882D4AB7D4";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "sum_pr" -p "plusMinusAverage_group";
	rename -uid "958E8DA7-41B0-6737-A8C2-038B4A348AC5";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -3 0 0 ;
createNode mesh -n "sum_prShape" -p "sum_pr";
	rename -uid "963655C1-42CC-7224-4C4C-5CB6AE247AEE";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "subtract_maya" -p "plusMinusAverage_group";
	rename -uid "FE0AC7CB-4CA2-48A4-8092-F290D53F4EED";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -2 0 -1 ;
createNode mesh -n "subtract_mayaShape" -p "subtract_maya";
	rename -uid "6EE72D28-4EC1-67FD-98B3-F296B4BA3406";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "subtract_pr" -p "plusMinusAverage_group";
	rename -uid "9FB92003-411B-2BCC-99CF-0387166F3838";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -2 0 0 ;
createNode mesh -n "subtract_prShape" -p "subtract_pr";
	rename -uid "340FEDAC-44B0-72DE-9F1F-9A990EF0F30E";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "average_maya" -p "plusMinusAverage_group";
	rename -uid "7B3E94AA-42C0-4AD3-014C-C1B43692276C";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -1 0.5 -1 ;
createNode mesh -n "average_mayaShape" -p "average_maya";
	rename -uid "C5A6A656-4FC4-934A-75BB-04AAE5635A98";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "average_pr" -p "plusMinusAverage_group";
	rename -uid "ADC7BE9F-4228-9E8D-EE1B-5C823EF67FC0";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -1 0 0 ;
createNode mesh -n "average_prShape" -p "average_pr";
	rename -uid "4F07A55B-4380-B9C6-AC3B-35A1F39764CD";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "sum_pr_static" -p "plusMinusAverage_group";
	rename -uid "10538E72-408D-A005-E899-9289DD47A579";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -3 0 1 ;
createNode mesh -n "sum_pr_staticShape" -p "sum_pr_static";
	rename -uid "CAB79808-4CDB-525C-B034-CB9415830D29";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "subtract_pr_static" -p "plusMinusAverage_group";
	rename -uid "EA6B3752-4CE3-3C9E-544C-228C7F1E8F2F";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -2 0 1 ;
createNode mesh -n "subtract_pr_staticShape" -p "subtract_pr_static";
	rename -uid "A91E8211-42A1-00DE-58C0-D9A63946EC42";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "average_pr_static" -p "plusMinusAverage_group";
	rename -uid "1183190F-4A72-7628-28DF-D085A9144259";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -1 0 1 ;
createNode mesh -n "average_pr_staticShape" -p "average_pr_static";
	rename -uid "32B210C1-4A5C-C2B4-27B7-A38CE347B51C";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "multiplyDivide_group" -p "cubes";
	rename -uid "09BD4D61-4DF4-8349-CB4B-75ADF0EC3D0D";
createNode transform -n "multiply_maya" -p "multiplyDivide_group";
	rename -uid "DA33DB09-49E3-3587-63B4-52A65759F4F1";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 1 0.25 -1 ;
createNode mesh -n "multiply_mayaShape" -p "multiply_maya";
	rename -uid "7ABCCE8C-4B8E-21F9-8789-1BB41D12F5D7";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "multiply_pr" -p "multiplyDivide_group";
	rename -uid "BA70D297-4792-99EC-4C3C-8AB900BC8F5D";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 1 0 0 ;
createNode mesh -n "multiply_prShape" -p "multiply_pr";
	rename -uid "8A4D19A1-4026-7E00-295F-2E809E4ABAA6";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "divide_maya" -p "multiplyDivide_group";
	rename -uid "4694B681-4200-7FF4-008E-D4B547529CCA";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 2 1 -1 ;
createNode mesh -n "divide_mayaShape" -p "divide_maya";
	rename -uid "1C9A2155-493D-A064-C1AC-B3959ABAE526";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "divide_pr" -p "multiplyDivide_group";
	rename -uid "77797EFA-4BF2-35DD-78F4-02A245EE4DD6";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 2 0 0 ;
createNode mesh -n "divide_prShape" -p "divide_pr";
	rename -uid "3EDA0CBD-4A5F-A70E-8C9B-649C3BBDB531";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "power_maya" -p "multiplyDivide_group";
	rename -uid "1A250F85-4DB3-E4DC-6073-32831F61AC40";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 3 0.70710676908493042 -1 ;
createNode mesh -n "power_mayaShape" -p "power_maya";
	rename -uid "CBECBCCB-4AB6-44C0-4C01-3A987A56DC87";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "power_pr" -p "multiplyDivide_group";
	rename -uid "3C56C452-4C6A-D41D-AB89-A0BE866459A0";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 3 0 0 ;
createNode mesh -n "power_prShape" -p "power_pr";
	rename -uid "510E9CFA-49DD-6BA2-D97D-50BE07CEDC73";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "multiply_pr_static" -p "multiplyDivide_group";
	rename -uid "7FF92728-475D-526E-F7B4-1EAFD4D10ABB";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 1 0 1 ;
createNode mesh -n "multiply_pr_staticShape" -p "multiply_pr_static";
	rename -uid "3553C927-49A3-FE0F-C1F7-CBB5CB4ACB25";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "divide_pr_static" -p "multiplyDivide_group";
	rename -uid "3ECD153D-489B-88EE-5F0B-AD8CFB55A790";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 2 0 1 ;
createNode mesh -n "divide_pr_staticShape" -p "divide_pr_static";
	rename -uid "C6127473-410C-52CE-C6D4-FEA450E8B077";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "power_pr_static" -p "multiplyDivide_group";
	rename -uid "90A24FB0-47A8-04DC-B33C-A5A86EF29534";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 3 0 1 ;
createNode mesh -n "power_pr_staticShape" -p "power_pr_static";
	rename -uid "2FA5B418-4BFB-86B4-4B81-1CA15B7F666C";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "custom_group" -p "cubes";
	rename -uid "504BA888-47D1-A68B-C36B-DCBDC67CD62D";
	setAttr ".t" -type "double3" 2 0 -6 ;
createNode transform -n "root_pr" -p "custom_group";
	rename -uid "538EC09F-439F-9A18-122F-6EB51B9242F0";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 3 0 6 ;
createNode mesh -n "root_prShape" -p "root_pr";
	rename -uid "18792EBD-4898-389F-B1E1-DB81B2980863";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "floorDivision_pr" -p "custom_group";
	rename -uid "25F9C8D6-4AA8-DC63-C48F-3F85852D6433";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 4 0 6 ;
createNode mesh -n "floorDivision_prShape" -p "floorDivision_pr";
	rename -uid "B49557F2-481C-98DA-7314-E7AF56D43A12";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "modulo_pr" -p "custom_group";
	rename -uid "A8E088BF-453E-7A2F-E67D-4E84F47D5480";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 5 0 6 ;
createNode mesh -n "modulo_prShape" -p "modulo_pr";
	rename -uid "42639553-4F19-F793-54ED-60BED2765CE3";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "root_pr_static" -p "custom_group";
	rename -uid "E40EF500-4307-42F7-5AD7-3CA7F9D143A2";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 3 0 7 ;
createNode mesh -n "root_pr_staticShape" -p "root_pr_static";
	rename -uid "3B2B658C-46DD-7303-BF97-36957172BE3F";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "floorDivision_pr_static" -p "custom_group";
	rename -uid "4BDD14F7-48AD-F13A-1E70-83AEE25982D7";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 4 0 7 ;
createNode mesh -n "floorDivision_pr_staticShape" -p "floorDivision_pr_static";
	rename -uid "7B93142E-4C29-71C5-D23B-33A2E9A76F32";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "modulo_pr_static" -p "custom_group";
	rename -uid "21276C6D-4BC4-5A2E-C14F-BF80B2FAE543";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 5 0 7 ;
createNode mesh -n "modulo_pr_staticShape" -p "modulo_pr_static";
	rename -uid "E3B9D05F-4213-120F-3DFD-4F8A75F8F665";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0.15803221 0 -0.16473003 
		-0.15803221 0 -0.16473003 0.15803221 0 -0.16473003 -0.15803221 0 -0.16473003 0.15803221 
		0 0.16473003 -0.15803221 0 0.16473003 0.15803221 0 0.16473003 -0.15803221 0 0.16473003;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "1A7E2FE9-42D4-A83B-0D29-D8918727F09F";
	setAttr -s 9 ".lnk";
	setAttr -s 9 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "83A4571F-4753-8916-8E23-529888802596";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "6101C0DF-40DB-03DA-A4B3-82A108FFE786";
createNode displayLayerManager -n "layerManager";
	rename -uid "64DD11E5-4997-C74C-9045-0EB624F9E2AC";
createNode displayLayer -n "defaultLayer";
	rename -uid "66A8DFEB-4F0A-3D0A-BBD2-A0B1083D0264";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "7AF89EEC-467C-F9F3-F566-69AE44E28BF9";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "660A3E10-4A84-4A0F-46F0-23B959BC1E69";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "281A2647-42D8-3C7E-D68D-D3A9356B2851";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode blinn -n "noOperation_blinn1";
	rename -uid "019E6A86-4ED7-20C2-5308-1294CECC52F8";
	setAttr ".c" -type "float3" 0.077922076 0.077922076 0.077922076 ;
	setAttr ".sc" -type "float3" 0.19480519 0.19480519 0.19480519 ;
createNode shadingEngine -n "blinn1SG";
	rename -uid "5E912564-4F20-05EF-5E69-1792DF01E093";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "1ED4D643-4D79-6679-FAF0-77B72620C098";
createNode blinn -n "sum_blinn2";
	rename -uid "89922247-4C55-7935-FB13-F5BAE98ACAE7";
	setAttr ".c" -type "float3" 1 0 0 ;
	setAttr ".sc" -type "float3" 0.19480519 0.19480519 0.19480519 ;
createNode shadingEngine -n "blinn2SG";
	rename -uid "A0C357D8-464F-A2CE-AD44-ECA0EBD926D2";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "E48EB726-43BD-B8EC-8869-D0864FF4CF44";
createNode blinn -n "subtract_blinn3";
	rename -uid "A9AD78D1-4D37-9848-8458-1F88D4D281EB";
	setAttr ".c" -type "float3" 0 1 0 ;
	setAttr ".sc" -type "float3" 0.19480519 0.19480519 0.19480519 ;
createNode shadingEngine -n "blinn3SG";
	rename -uid "BA17B37B-4187-5088-DB27-9D8E2B45B243";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo3";
	rename -uid "3D01DB63-48F8-38EC-EFE8-DAAF869A790C";
createNode blinn -n "average_blinn4";
	rename -uid "3F22286C-43B0-3E83-2711-999F7902C7E6";
	setAttr ".c" -type "float3" 0 0 1 ;
	setAttr ".sc" -type "float3" 0.19480519 0.19480519 0.19480519 ;
createNode shadingEngine -n "blinn4SG";
	rename -uid "777256DA-4C54-8883-FD79-1CA29D5FE9EB";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo4";
	rename -uid "2EC6A7D7-4700-A58B-4310-D2958FCD941E";
createNode blinn -n "multiply_blinn3";
	rename -uid "CAE84E5C-45FA-318C-0DF4-EEBC9FD06D39";
	setAttr ".c" -type "float3" 0.17482518 0 0 ;
	setAttr ".sc" -type "float3" 0.19480519 0.19480519 0.19480519 ;
createNode blinn -n "divide_blinn4";
	rename -uid "23358DBE-4B12-6B9D-5924-0D85DFA3F05C";
	setAttr ".c" -type "float3" 0 0.16783217 0 ;
	setAttr ".sc" -type "float3" 0.19480519 0.19480519 0.19480519 ;
createNode blinn -n "power_blinn5";
	rename -uid "DAE6CA28-43B0-BD88-E3E6-31A255F7884D";
	setAttr ".c" -type "float3" 0 0 0.23076923 ;
	setAttr ".sc" -type "float3" 0.19480519 0.19480519 0.19480519 ;
createNode shadingEngine -n "subtract_blinn4SG";
	rename -uid "A0FBCF54-489F-6D9D-C7E0-67BD8C76CD71";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo5";
	rename -uid "20BAC9C2-4797-ADFF-D5FA-A080BAA42DCC";
createNode shadingEngine -n "sum_blinn3SG";
	rename -uid "EDFE1DF7-4019-648A-F2D9-00B3544C4BAD";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo6";
	rename -uid "73E2249D-4467-3B93-E711-DFB2FBA4EE24";
createNode shadingEngine -n "power_blinn5SG";
	rename -uid "580525C0-4B6F-74FD-6241-08853E780029";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo7";
	rename -uid "EA446CD0-427C-BBF9-834E-A2AE9876021F";
createNode multiplyDivide -n "noOperation_multiplyDivide";
	rename -uid "EE297CE7-454B-0CE6-B02F-89BE5401EDEC";
	setAttr ".op" 0;
	setAttr ".i2" -type "float3" 0.5 1.1 1 ;
createNode multiplyDivide -n "multiply_multiplyDivide";
	rename -uid "125B4CAC-4D84-B853-747A-90B30DA18A52";
	setAttr ".i2" -type "float3" 0.5 1.1 1 ;
createNode multiplyDivide -n "divide_multiplyDivide";
	rename -uid "9582DF9C-4220-17AC-947D-9491900D5F56";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 0.5 1.1 1 ;
createNode multiplyDivide -n "power_multiplyDivide";
	rename -uid "C60844EA-40F7-E536-8315-C58AB92BADF3";
	setAttr ".op" 3;
	setAttr ".i2" -type "float3" 0.5 1.1 1 ;
createNode plusMinusAverage -n "average_plusMinusAverage";
	rename -uid "1886D9B4-4C51-5445-6820-5FADE98285ED";
	setAttr ".op" 3;
	setAttr -s 2 ".i1[1]"  0.5;
	setAttr ".i2[0]" -type "float2" 0 0;
createNode plusMinusAverage -n "subtract_plusMinusAverage";
	rename -uid "63A0C01E-43B7-D4A7-41C8-919F23ABB31D";
	setAttr ".op" 2;
	setAttr -s 2 ".i1[1]"  0.5;
	setAttr ".i2[0]" -type "float2" 0 0;
createNode addDoubleLinear -n "addDoubleLinear";
	rename -uid "D2B39C82-4C20-B92E-48A2-D088BDF06255";
	setAttr ".i2" 0.5;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "1E4178F4-452A-7AF0-BED4-A39D688D8B84";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -176.19046918929598 -795.26766111134634 ;
	setAttr ".tgi[0].vh" -type "double2" 770.23806463158451 658.36290464669082 ;
	setAttr -s 12 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -250;
	setAttr ".tgi[0].ni[0].y" 190;
	setAttr ".tgi[0].ni[0].nvs" 1923;
	setAttr ".tgi[0].ni[1].x" 358.57144165039063;
	setAttr ".tgi[0].ni[1].y" 610;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" -250;
	setAttr ".tgi[0].ni[2].y" 190;
	setAttr ".tgi[0].ni[2].nvs" 1923;
	setAttr ".tgi[0].ni[3].x" 358.57144165039063;
	setAttr ".tgi[0].ni[3].y" -305.71429443359375;
	setAttr ".tgi[0].ni[3].nvs" 1923;
	setAttr ".tgi[0].ni[4].x" 57.142856597900391;
	setAttr ".tgi[0].ni[4].y" 190;
	setAttr ".tgi[0].ni[4].nvs" 1923;
	setAttr ".tgi[0].ni[5].x" 51.428569793701172;
	setAttr ".tgi[0].ni[5].y" -307.14285278320313;
	setAttr ".tgi[0].ni[5].nvs" 1923;
	setAttr ".tgi[0].ni[6].x" -250;
	setAttr ".tgi[0].ni[6].y" 190;
	setAttr ".tgi[0].ni[6].nvs" 1923;
	setAttr ".tgi[0].ni[7].x" 571.4285888671875;
	setAttr ".tgi[0].ni[7].y" 265.71429443359375;
	setAttr ".tgi[0].ni[7].nvs" 1923;
	setAttr ".tgi[0].ni[8].x" 51.428569793701172;
	setAttr ".tgi[0].ni[8].y" 608.5714111328125;
	setAttr ".tgi[0].ni[8].nvs" 1923;
	setAttr ".tgi[0].ni[9].x" 57.142856597900391;
	setAttr ".tgi[0].ni[9].y" 190;
	setAttr ".tgi[0].ni[9].nvs" 1923;
	setAttr ".tgi[0].ni[10].x" 57.142856597900391;
	setAttr ".tgi[0].ni[10].y" 190;
	setAttr ".tgi[0].ni[10].nvs" 1923;
	setAttr ".tgi[0].ni[11].x" 264.28570556640625;
	setAttr ".tgi[0].ni[11].y" 264.28570556640625;
	setAttr ".tgi[0].ni[11].nvs" 1923;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "412534DA-4A5F-9364-9CA1-FFBB32063B0C";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -921.22054480769043 1521.2332334763305 ;
	setAttr ".tgi[0].vh" -type "double2" 2188.9062211888972 3040.3602777918904 ;
	setAttr -s 24 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 1050;
	setAttr ".tgi[0].ni[0].y" 461.42855834960938;
	setAttr ".tgi[0].ni[0].nvs" 18305;
	setAttr ".tgi[0].ni[1].x" 1050;
	setAttr ".tgi[0].ni[1].y" 622.85711669921875;
	setAttr ".tgi[0].ni[1].nvs" 18305;
	setAttr ".tgi[0].ni[2].x" 1050;
	setAttr ".tgi[0].ni[2].y" 784.28570556640625;
	setAttr ".tgi[0].ni[2].nvs" 18305;
	setAttr ".tgi[0].ni[3].x" 1050;
	setAttr ".tgi[0].ni[3].y" 945.71429443359375;
	setAttr ".tgi[0].ni[3].nvs" 18305;
	setAttr ".tgi[0].ni[4].x" 1050;
	setAttr ".tgi[0].ni[4].y" 3158.571533203125;
	setAttr ".tgi[0].ni[4].nvs" 18305;
	setAttr ".tgi[0].ni[5].x" 731.4285888671875;
	setAttr ".tgi[0].ni[5].y" 2381.428466796875;
	setAttr ".tgi[0].ni[5].nvs" 18305;
	setAttr ".tgi[0].ni[6].x" 731.4285888671875;
	setAttr ".tgi[0].ni[6].y" 2981.428466796875;
	setAttr ".tgi[0].ni[6].nvs" 18306;
	setAttr ".tgi[0].ni[7].x" 424.28570556640625;
	setAttr ".tgi[0].ni[7].y" 2537.142822265625;
	setAttr ".tgi[0].ni[7].nvs" 18306;
	setAttr ".tgi[0].ni[8].x" 1050;
	setAttr ".tgi[0].ni[8].y" 2958.571533203125;
	setAttr ".tgi[0].ni[8].nvs" 18305;
	setAttr ".tgi[0].ni[9].x" 1050;
	setAttr ".tgi[0].ni[9].y" 2758.571533203125;
	setAttr ".tgi[0].ni[9].nvs" 18305;
	setAttr ".tgi[0].ni[10].x" 1050;
	setAttr ".tgi[0].ni[10].y" 1107.142822265625;
	setAttr ".tgi[0].ni[10].nvs" 18305;
	setAttr ".tgi[0].ni[11].x" 1050;
	setAttr ".tgi[0].ni[11].y" 2558.571533203125;
	setAttr ".tgi[0].ni[11].nvs" 18305;
	setAttr ".tgi[0].ni[12].x" 731.4285888671875;
	setAttr ".tgi[0].ni[12].y" 1981.4285888671875;
	setAttr ".tgi[0].ni[12].nvs" 18305;
	setAttr ".tgi[0].ni[13].x" 1050;
	setAttr ".tgi[0].ni[13].y" 1268.5714111328125;
	setAttr ".tgi[0].ni[13].nvs" 18305;
	setAttr ".tgi[0].ni[14].x" 1050;
	setAttr ".tgi[0].ni[14].y" 2358.571533203125;
	setAttr ".tgi[0].ni[14].nvs" 18305;
	setAttr ".tgi[0].ni[15].x" 1050;
	setAttr ".tgi[0].ni[15].y" 1430;
	setAttr ".tgi[0].ni[15].nvs" 18305;
	setAttr ".tgi[0].ni[16].x" 1050;
	setAttr ".tgi[0].ni[16].y" 1591.4285888671875;
	setAttr ".tgi[0].ni[16].nvs" 18305;
	setAttr ".tgi[0].ni[17].x" 1050;
	setAttr ".tgi[0].ni[17].y" 2158.571533203125;
	setAttr ".tgi[0].ni[17].nvs" 18305;
	setAttr ".tgi[0].ni[18].x" 731.4285888671875;
	setAttr ".tgi[0].ni[18].y" 2581.428466796875;
	setAttr ".tgi[0].ni[18].nvs" 18305;
	setAttr ".tgi[0].ni[19].x" 731.4285888671875;
	setAttr ".tgi[0].ni[19].y" 2781.428466796875;
	setAttr ".tgi[0].ni[19].nvs" 18305;
	setAttr ".tgi[0].ni[20].x" 731.4285888671875;
	setAttr ".tgi[0].ni[20].y" 3181.428466796875;
	setAttr ".tgi[0].ni[20].nvs" 18305;
	setAttr ".tgi[0].ni[21].x" 1050;
	setAttr ".tgi[0].ni[21].y" 1958.5714111328125;
	setAttr ".tgi[0].ni[21].nvs" 18305;
	setAttr ".tgi[0].ni[22].x" 731.4285888671875;
	setAttr ".tgi[0].ni[22].y" 2181.428466796875;
	setAttr ".tgi[0].ni[22].nvs" 18305;
	setAttr ".tgi[0].ni[23].x" 1050;
	setAttr ".tgi[0].ni[23].y" 1752.857177734375;
	setAttr ".tgi[0].ni[23].nvs" 18305;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 9 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 11 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 7 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 6 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "noOperation_multiplyDivide.ox" "noOperation_maya.ty";
connectAttr "addDoubleLinear.o" "sum_maya.ty";
connectAttr "subtract_plusMinusAverage.o1" "subtract_maya.ty";
connectAttr "average_plusMinusAverage.o1" "average_maya.ty";
connectAttr "multiply_multiplyDivide.ox" "multiply_maya.ty";
connectAttr "divide_multiplyDivide.ox" "divide_maya.ty";
connectAttr "power_multiplyDivide.ox" "power_maya.ty";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn3SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn4SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "subtract_blinn4SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "sum_blinn3SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "power_blinn5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn4SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "subtract_blinn4SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "sum_blinn3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "power_blinn5SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "noOperation_blinn1.oc" "blinn1SG.ss";
connectAttr "noOperation_mayaShape.iog" "blinn1SG.dsm" -na;
connectAttr "noOperation_prShape.iog" "blinn1SG.dsm" -na;
connectAttr "noOperation_pr_staticShape.iog" "blinn1SG.dsm" -na;
connectAttr "blinn1SG.msg" "materialInfo1.sg";
connectAttr "noOperation_blinn1.msg" "materialInfo1.m";
connectAttr "sum_blinn2.oc" "blinn2SG.ss";
connectAttr "sum_mayaShape.iog" "blinn2SG.dsm" -na;
connectAttr "sum_prShape.iog" "blinn2SG.dsm" -na;
connectAttr "sum_pr_staticShape.iog" "blinn2SG.dsm" -na;
connectAttr "blinn2SG.msg" "materialInfo2.sg";
connectAttr "sum_blinn2.msg" "materialInfo2.m";
connectAttr "subtract_blinn3.oc" "blinn3SG.ss";
connectAttr "subtract_mayaShape.iog" "blinn3SG.dsm" -na;
connectAttr "subtract_prShape.iog" "blinn3SG.dsm" -na;
connectAttr "subtract_pr_staticShape.iog" "blinn3SG.dsm" -na;
connectAttr "blinn3SG.msg" "materialInfo3.sg";
connectAttr "subtract_blinn3.msg" "materialInfo3.m";
connectAttr "average_blinn4.oc" "blinn4SG.ss";
connectAttr "average_prShape.iog" "blinn4SG.dsm" -na;
connectAttr "average_mayaShape.iog" "blinn4SG.dsm" -na;
connectAttr "average_pr_staticShape.iog" "blinn4SG.dsm" -na;
connectAttr "blinn4SG.msg" "materialInfo4.sg";
connectAttr "average_blinn4.msg" "materialInfo4.m";
connectAttr "divide_blinn4.oc" "subtract_blinn4SG.ss";
connectAttr "divide_mayaShape.iog" "subtract_blinn4SG.dsm" -na;
connectAttr "divide_prShape.iog" "subtract_blinn4SG.dsm" -na;
connectAttr "divide_pr_staticShape.iog" "subtract_blinn4SG.dsm" -na;
connectAttr "subtract_blinn4SG.msg" "materialInfo5.sg";
connectAttr "divide_blinn4.msg" "materialInfo5.m";
connectAttr "multiply_blinn3.oc" "sum_blinn3SG.ss";
connectAttr "multiply_mayaShape.iog" "sum_blinn3SG.dsm" -na;
connectAttr "multiply_prShape.iog" "sum_blinn3SG.dsm" -na;
connectAttr "multiply_pr_staticShape.iog" "sum_blinn3SG.dsm" -na;
connectAttr "sum_blinn3SG.msg" "materialInfo6.sg";
connectAttr "multiply_blinn3.msg" "materialInfo6.m";
connectAttr "power_blinn5.oc" "power_blinn5SG.ss";
connectAttr "power_mayaShape.iog" "power_blinn5SG.dsm" -na;
connectAttr "power_prShape.iog" "power_blinn5SG.dsm" -na;
connectAttr "power_pr_staticShape.iog" "power_blinn5SG.dsm" -na;
connectAttr "power_blinn5SG.msg" "materialInfo7.sg";
connectAttr "power_blinn5.msg" "materialInfo7.m";
connectAttr "locator.ty" "noOperation_multiplyDivide.i1x";
connectAttr "locator.ty" "noOperation_multiplyDivide.i1y";
connectAttr "locator.ty" "multiply_multiplyDivide.i1x";
connectAttr "locator.ty" "multiply_multiplyDivide.i1y";
connectAttr "locator.ty" "divide_multiplyDivide.i1x";
connectAttr "locator.ty" "divide_multiplyDivide.i1y";
connectAttr "locator.ty" "power_multiplyDivide.i1x";
connectAttr "locator.ty" "power_multiplyDivide.i1y";
connectAttr "locator.ty" "average_plusMinusAverage.i1[0]";
connectAttr "locator.ty" "subtract_plusMinusAverage.i1[0]";
connectAttr "locator.ty" "addDoubleLinear.i1";
connectAttr "average_blinn4.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "subtract_blinn4SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "subtract_blinn3.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[2].dn"
		;
connectAttr "power_blinn5SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "blinn3SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "power_blinn5.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "sum_blinn2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "sum_blinn3SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[7].dn"
		;
connectAttr "divide_blinn4.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[8].dn"
		;
connectAttr "blinn4SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[9].dn"
		;
connectAttr "blinn2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "multiply_blinn3.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[11].dn"
		;
connectAttr "divide_pr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "noOperation_pr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "power_pr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "subtract_pr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn";
connectAttr "average_maya.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn";
connectAttr "divide_multiplyDivide.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "addDoubleLinear.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn";
connectAttr "locator.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn";
connectAttr "sum_maya.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn";
connectAttr "subtract_maya.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn";
connectAttr "modulo_pr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn";
connectAttr "multiply_maya.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn";
connectAttr "noOperation_multiplyDivide.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn"
		;
connectAttr "average_pr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn";
connectAttr "divide_maya.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn";
connectAttr "sum_pr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn";
connectAttr "multiply_pr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[16].dn";
connectAttr "power_maya.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[17].dn";
connectAttr "multiply_multiplyDivide.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[18].dn"
		;
connectAttr "subtract_plusMinusAverage.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[19].dn"
		;
connectAttr "average_plusMinusAverage.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[20].dn"
		;
connectAttr "noOperation_maya.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[21].dn"
		;
connectAttr "power_multiplyDivide.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[22].dn"
		;
connectAttr "floorDivision_pr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[23].dn"
		;
connectAttr "blinn1SG.pa" ":renderPartition.st" -na;
connectAttr "blinn2SG.pa" ":renderPartition.st" -na;
connectAttr "blinn3SG.pa" ":renderPartition.st" -na;
connectAttr "blinn4SG.pa" ":renderPartition.st" -na;
connectAttr "subtract_blinn4SG.pa" ":renderPartition.st" -na;
connectAttr "sum_blinn3SG.pa" ":renderPartition.st" -na;
connectAttr "power_blinn5SG.pa" ":renderPartition.st" -na;
connectAttr "noOperation_blinn1.msg" ":defaultShaderList1.s" -na;
connectAttr "sum_blinn2.msg" ":defaultShaderList1.s" -na;
connectAttr "subtract_blinn3.msg" ":defaultShaderList1.s" -na;
connectAttr "average_blinn4.msg" ":defaultShaderList1.s" -na;
connectAttr "multiply_blinn3.msg" ":defaultShaderList1.s" -na;
connectAttr "divide_blinn4.msg" ":defaultShaderList1.s" -na;
connectAttr "power_blinn5.msg" ":defaultShaderList1.s" -na;
connectAttr "noOperation_multiplyDivide.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multiply_multiplyDivide.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "divide_multiplyDivide.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "power_multiplyDivide.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "average_plusMinusAverage.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "subtract_plusMinusAverage.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "floorDivision_prShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "modulo_prShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "root_prShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "root_pr_staticShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "floorDivision_pr_staticShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "modulo_pr_staticShape.iog" ":initialShadingGroup.dsm" -na;
// End of test_prScalarMath.ma
